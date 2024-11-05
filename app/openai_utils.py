import openai
from .config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def analyze_compliance(data):
    prompt = f"Analyze the following compliance data for patterns: {data}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def generate_insights():
    prompt = "Provide suggestions for improving supplier compliance based on compliance history."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
