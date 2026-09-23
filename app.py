from google import genai
from dotenv import load_dotenv
import os
import requests
import json
from google.genai import types
load_dotenv()
def convert_currency(amount, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    if data["result"] == "success":
        rate = data["rates"][to_currency]
        converted_amount = amount * rate
        return {
        "rate": rate,
        "converted_amount": converted_amount
        }
    else:
        return {
        "error": "Failed to fetch exchange rate"
        }

    
tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="convert_currency",
            description="Convert an amount from one currency to another using live exchange rates.",
            parameters={
                "type": "OBJECT",
                "properties": {
                    "amount": {
                        "type": "NUMBER",
                        "description": "Amount to convert"
                    },
                    "from_currency": {
                        "type": "STRING",
                        "description": "Currency to convert from, such as USD"
                    },
                    "to_currency": {
                        "type": "STRING",
                        "description": "Currency to convert to, such as INR"
                    }
                },
                "required": [
                    "amount",
                    "from_currency",
                    "to_currency"
                ]
            }
        )
    ]
)


client=genai.Client(api_key=os.getenv('API_KEY'))
message = input("Enter conversion: ")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=message,
    config=types.GenerateContentConfig(
        tools=[tool]
    )
)
function_call = None

for part in response.candidates[0].content.parts:
    if part.function_call:
        function_call = part.function_call
        break

if function_call:
    args = function_call.args

    result = convert_currency(
        args["amount"],
        args["from_currency"],
        args["to_currency"]
    )

    tool_response = types.Part.from_function_response(
        name=function_call.name,
        response=result
    )

    final_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            message,
            response.candidates[0].content,
            tool_response
        ]
    )

    print(final_response.text)