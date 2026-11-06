# Structured Data Extractor using Gemini API

## Project Overview
The Structured Data Extractor is a Python application that uses Google's Gemini API to convert unstructured text into structured JSON data.

It supports three document types: Receipts, Emails, and Articles.

## Features
- Extract structured information from receipts.
- Extract sender, recipient, date, subject, and body from emails.
- Extract title, author, publication date, and summary from articles.
- Validate structured output using Pydantic.
- Save extracted information as JSON files.

## Technologies Used
- Python
- Google Gemini API
- Pydantic
- JSON
- Poetry

## Project Structure

```text
structured-data-extractor/
├── main.py
├── schemas.py
├── test_schemas.py
├── test_validation.py
├── pyproject.toml
├── poetry.lock
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd structured-data-extractor
```

Install dependencies:

```bash
poetry install
```

Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run the Project

```bash
poetry run python main.py
```

Select a document type:

1. Receipt
2. Email
3. Article

Enter the unstructured text and receive structured JSON output.

## Learning Outcomes
- Gemini API integration
- Structured output generation
- Pydantic schema validation
- JSON serialization and file handling

## Author
LLM Development Learner