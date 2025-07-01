import os
from dotenv import load_dotenv
from openai import OpenAI
from search_tools import search_google


# Load API keys from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")

client = OpenAI(api_key=api_key)

#Function: Use GPT to summarize real-time web search results
def search_and_summarize(topic):
    print("🔍 Searching Google...")
    raw_results = search_google(topic)

    prompt = f"""
You are an intelligent research assistant.
Summarize the following search results about "{topic}" into a clear, concise, and structured explanation suitable for a beginner.

Search Results:
{raw_results}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )

    return response.choices[0].message.content

# Main Program
if __name__ == "__main__":
    topic = input("Enter your research topic: ")
    print("\n🤖 Here’s your learning plan:\n")
    print(search_and_summarize(topic))