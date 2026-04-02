import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBb1iAMcAPb-v5zIFU0i4UiZHw4N_Zi__o")

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("Hello")
print(response.text)
