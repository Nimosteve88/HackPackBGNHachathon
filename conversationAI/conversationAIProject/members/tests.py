from django.test import TestCase
import os
import openai
print("hello")
openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful AI Tutor."},
        {"role": "user", "content": "I am Pradip, I want to learn AI"},
        {"role": "assistant", "content": "Hello, Pradip Thats awesome, what do you want to know aboout AI"},
        {"role": "user", "content": "What is NLP?"}
    ]
)

# Print the model's response
print(response.choices[0].text)