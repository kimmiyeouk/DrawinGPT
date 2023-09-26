import openai
from DrawinGPT_Modules.import_apikey import Import_APIkey

def Generate_image(prompt):
    openai.api_key = Import_APIkey()

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']
    return image_url