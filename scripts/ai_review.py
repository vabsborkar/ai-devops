import os
import google.generativeai as genai

api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check GitHub Secrets.")

genai.configure(api_key=api_key)

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

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    return response.text


if __name__ == "__main__":
    with open("diff.txt", "r") as f:
        diff = f.read()

    review = review_code(diff)

    with open("review.txt", "w") as f:
        f.write(review)

    print("AI Review Completed")
