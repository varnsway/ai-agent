import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables from .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]

model = "gemini-2.0-flash-001"


result = client.models.generate_content(model=model, contents=messages)
prompt_tokens = result.usage_metadata.prompt_token_count
response_tokens = result.usage_metadata.candidates_token_count


def main():
    if len(sys.argv) > 2:
        print("Error: invalid number of arguments.")
        sys.exit(1)
    print(result.text)
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
