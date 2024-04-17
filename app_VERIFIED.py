from openai import OpenAI


client = OpenAI(api_key="sk-proj-PpTc69KyUScp3LnanH3ZT3BlbkFJERQCmwjTarFPrynfpmiz")

USER_PROMPT = "Can you explain chemical bonding?"
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful education assistant who knows a lot about Physics, Chemistry, "
                                  "Biology and other relevant courses offered in colleges. Give answers that are "
                                  "understandable and clear"},
    {"role": "user", "content": "Which great Scientist developed Special Relativity?"},
    {"role": "assistant", "content": "Special Relativity was developed by Albert Einstein"},
    {"role": "user", "content": USER_PROMPT}
    ]



)

USER_RESPONSE = response.choices[0].message.content
print(USER_RESPONSE)
