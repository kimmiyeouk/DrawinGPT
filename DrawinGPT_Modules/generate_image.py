import openai

def Generate_image(prompt, api_key):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']
    return image_url