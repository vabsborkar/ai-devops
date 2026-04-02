import os
from google import genai

api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check GitHub Secrets.")

client = genai.Client(api_key=api_key)

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
        model="gemini-pro",
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
        print("Critical issue found.")
    else:
        print("No critical issues.")
