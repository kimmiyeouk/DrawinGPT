'''

DrawinGPT 0.1.1 Alpha

This is PyKakao and OpenAI GPT-3.5-turbo project

by. Kimmiyeouk
Commited in 2023/09/25
All rights reserved.

Github: https://github.com/kimmiyeouk

'''


import openai
#import googletrans
import pypapago

from PyKakao import Karlo
from DrawinGPT_Modules.generate_image import Generate_image
from DrawinGPT_Modules.generate_text import Generate_text
from DrawinGPT_Modules.import_apikey import Import_APIkey

while True:
    cmd = input('처리할 명령이 무엇인가요?(그림/대화): ')

    if cmd == '대화':
        prompt = input('Q: ')

        #gpt-3.5-turbo 엔진으로 언어 모델 구현
        response = Generate_text(prompt)

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
        print(Generate_image(str(prompt)))
