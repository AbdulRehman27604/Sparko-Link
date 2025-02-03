import openai

import Send_email
import Speech_Input

openai.api_key=""
def generate_email_content(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    print(response.choices[0].message.content.strip())
    return response.choices[0].message.content.strip()
