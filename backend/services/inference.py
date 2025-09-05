from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),  # Store your API key in env var
)

def explain_code(code: str) -> str:
    """
    Use OpenRouter API to explain code in plain English.
    """
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://127.0.0.1:8000/",  # change to your site later
                "X-Title": "AI Code Understanding",        # change if you want
            },
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert software engineer who explains code clearly in plain English."
                },
                {
                    "role": "user",
                    "content": f"Explain what the following Python code does:\n{code}"
                }
            ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error during explanation: {str(e)}]"
