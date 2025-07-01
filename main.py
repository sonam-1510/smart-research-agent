import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API keys from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")

client = OpenAI(api_key=api_key)

# Function to generate research steps using GPT-4
def plan_research_steps(topic):
    prompt = f"""
    You are a smart research assistant. I want to learn about "{topic}".
    Break this down into 5 logical learning steps I should follow, starting from beginner level.
    Be clear and concise.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while generating research steps: {e}"

# Entry point of the script
if __name__ == "__main__":
    topic = input("Enter your research topic: ")
    steps = plan_research_steps(topic)
    print("\nHere’s your learning plan:\n")
    print(steps)