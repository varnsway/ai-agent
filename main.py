import os
from dotenv import load_dotenv
from google import genai


# Load environment variables from .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"
contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

result = client.models.generate_content(model=model, contents=contents)
prompt_tokens = result.usage_metadata.prompt_token_count
response_tokens = result.usage_metadata.candidates_token_count


def main():
    print(result.text)
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
