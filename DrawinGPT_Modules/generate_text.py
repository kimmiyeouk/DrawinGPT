import openai

def Generate_text(prompt,api_key):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "hello. your name is DrawinGPT. And you have to say honorific to user."},
        {"role": "user", "content": prompt}])

    response = completion.choices[0].message.content
    return response