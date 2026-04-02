import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def review_code(diff):
    prompt = f"""
You are a senior DevOps engineer.

Review the following code diff and:
- Identify bugs
- Suggest improvements
- Highlight security risks

Code:
{diff}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    with open("diff.txt", "r") as f:
        diff = f.read()

    review = review_code(diff)

    with open("review.txt", "w") as f:
        f.write(review)

    if "critical" in review.lower():
        print("Critical issue found. Failing pipeline.")
        exit(1)

