# Currency Converter with Tool Calling

A Python-based Currency Converter Assistant using **Google Gemini API Function Calling** and a **live Exchange Rate API**.

## 🚀 Features

* Converts currencies using live exchange rates
* Uses Gemini for tool/function calling
* Gemini automatically identifies the required currencies and amount
* Fetches live exchange rates from Exchange Rate API
* Generates a short, human-readable final response

## 🛠️ Tech Stack

* Python
* Google Gemini API
* Gemini Function Calling
* Exchange Rate API
* Requests
* python-dotenv

## 📂 Project Structure

```text
CurrencyConverter/
├── app.py
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Setup

Install the required packages:

```bash
pip install google-genai python-dotenv requests
```

Create a `.env` file:

```env
API_KEY="your_gemini_api_key"
```

**Do not upload `.env`**
