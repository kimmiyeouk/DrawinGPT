'''

DrawinGPT 0.1.0 Alpha

This is PyKakao and OpenAI GPT-3.5-turbo project

by. Kimmiyeouk
Commited in 2023/09/22
All rights reserved.

Github: https://github.com/kimmiyeouk

'''


import openai
#import googletrans
import pypapago

from PyKakao import Karlo

openai.api_key = '' #Please enter OpenAI API key here.

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )

    image_url = response['data'][0]['url']
    return image_url

def generate_text(prompt):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "hello. your name is DrawinGPT. And you have to say honorific to user."},
        {"role": "user", "content": prompt}])

    response = completion.choices[0].message.content
    return response
while True:
    cmd = input('처리할 명령이 무엇인가요?(그림/대화): ')

    if cmd == '대화':
        prompt = input('Q: ')

        #gpt-3.5-turbo 엔진으로 언어 모델 구현
        response = generate_text(prompt)

        print(f'A: {response}')
    else:
        prompt = input('원하는 그림: ')
        prompt = prompt.rstrip('\n')
        #
        # #번역
        # translator = pypapago.Translator()
        # prompt = translator.translate(prompt, 'ko', 'en')
        #
        # print(prompt)
        print(generate_image(str(prompt.text)))