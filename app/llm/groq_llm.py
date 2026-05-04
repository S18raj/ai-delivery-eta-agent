import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def compress_context(condition, delay):
    return f"{condition} | {delay}h"

def generate_llm_explanation(condition, delay):

    compressed_context = compress_context(condition, delay)

    prompt = f"""
Explain this delivery delay professionally.

Context: {compressed_context}

Short response only.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content