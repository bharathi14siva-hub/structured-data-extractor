
import os
import json
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from schemas import Receipt, Email, Article


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# Initialize Gemini client
client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=60000)
)

MODEL_NAME = "gemini-3.5-flash-lite"


# Extract structured data using Gemini
def extract_data(text, schema):

    prompt = f"""
You are an expert structured data extraction system.

Your task is to extract accurate information from the input text.

IMPORTANT RULES:

1. Read the complete input carefully.
2. Extract every available piece of information.
3. Never ignore information clearly present in the text.
4. Do not invent or assume information.
5. For missing string values, use "Unknown".
6. For missing numerical values, use null.
7. Extract every item when processing a receipt.
8. Preserve the original amounts and currency.
9. Follow the provided response schema exactly.

INPUT TEXT:

{text}
"""

    max_retries = 3

    for attempt in range(max_retries):

        try:

            print("\nSending text to Gemini API...", flush=True)

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=schema,
                    temperature=0
                )
            )

            print("\nGemini response received!", flush=True)

            # Extract parsed response
            if response.parsed is not None:

                if hasattr(response.parsed, "model_dump"):

                    result = response.parsed.model_dump()

                else:

                    result = response.parsed

                return json.dumps(
                    result,
                    indent=4,
                    ensure_ascii=False
                )

            # Fallback to raw JSON
            if response.text:

                data = json.loads(response.text)

                return json.dumps(
                    data,
                    indent=4,
                    ensure_ascii=False
                )

            raise ValueError(
                "Gemini returned an empty response."
            )

        except Exception as e:

            error_message = str(e)

            print(
                f"\nAPI attempt {attempt + 1} failed: {error_message}",
                flush=True
            )

            # Handle API quota errors
            if "429" in error_message:

                raise Exception(
                    "Gemini API quota or rate limit exceeded. "
                    "Check your API usage."
                ) from e

            # Handle temporary server errors
            elif any(
                code in error_message
                for code in ["500", "502", "503", "504"]
            ):

                if attempt < max_retries - 1:

                    wait_time = 2 ** (attempt + 1)

                    print(
                        f"Retrying in {wait_time} seconds...",
                        flush=True
                    )

                    time.sleep(wait_time)

                else:

                    raise Exception(
                        "Gemini server is temporarily unavailable. "
                        "Please try again later."
                    ) from e

            else:

                raise


# Collect user input
def get_user_input():

    print("\nEnter your unstructured text.")
    print("Press Enter twice to finish:\n")

    lines = []
    empty_count = 0

    while True:

        line = input()

        if line.strip() == "":

            empty_count += 1

            if empty_count == 2:
                break

            lines.append("")
            continue

        empty_count = 0
        lines.append(line)

    return "\n".join(lines).strip()


# Save extracted JSON
def save_json(result, choice):

    filenames = {
        "1": "receipt.json",
        "2": "email.json",
        "3": "article.json"
    }

    os.makedirs("output", exist_ok=True)

    file_path = os.path.join(
        "output",
        filenames[choice]
    )

    data = json.loads(result)

    with open(file_path, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"\nJSON saved successfully: {file_path}"
    )


# Main function
def main():

    print("\nSTRUCTURED DATA EXTRACTOR")

    print("1. Receipt")
    print("2. Email")
    print("3. Article")

    choice = input("\nSelect document type: ").strip()

    schemas = {
        "1": Receipt,
        "2": Email,
        "3": Article
    }

    # Validate document type
    if choice not in schemas:

        print("\nInvalid choice!")
        return

    # Collect user input
    text = get_user_input()

    if not text:

        print("\nPlease provide some text!")
        return

    # Extract and save structured data
    try:

        result = extract_data(
            text,
            schemas[choice]
        )

        print("\nExtracted JSON:")
        print(result)

        save_json(result, choice)

    except Exception as e:

        print("\nError:", e)


if __name__ == "__main__":
    main()
