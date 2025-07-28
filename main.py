import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"
    verbose = False
    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]
    
    result = client.models.generate_content(model=model, contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt))
    prompt_tokens = result.usage_metadata.prompt_token_count
    response_tokens = result.usage_metadata.candidates_token_count
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            verbose = True
        else:
            print("Error: invalid number of arguments.")
            sys.exit(1)
    if verbose:
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    print(result.text)


if __name__ == "__main__":
    main()
