from sqlalchemy.orm import Session
from cloudinary.uploader import upload
import os
import openai
import requests
import cloudinary
import base64

CAPI_KEY=os.getenv("CLD_API_KEY")
CAPI_SECRET=os.getenv("CLD_API_SECRET")
MAPI_KEY=os.getenv("MIRAGE_API_KEY")
SAPI_KEY=os.getenv("STABILITY_API_KEY")

          
cloudinary.config( 
    cloud_name = "dtghsmx0s", api_key = CAPI_KEY, api_secret = CAPI_SECRET)

async def get_image_from_url_1(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
    )
    image_url = response["data"][0]["url"]

    image_data = requests.get(image_url).content
    upload_result = upload(image_data)
    if upload_result is None:
        return None
    return upload_result["url"]

async def get_image_from_url_2(prompt):
    API_URL = "https://api-inference.huggingface.co/models/MirageML/lowpoly-cyberpunk"
    headers = {"Authorization": f"Bearer {MAPI_KEY}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response
    reponse = query({
        "inputs": prompt,
    })
    if reponse.status_code != 200:
        return None
    image_bytes = reponse.content
    if image_bytes is None or len(image_bytes) == 0:
        return None
    upload_result = upload(image_bytes)
    if upload_result is None:
        return None
    return upload_result["url"] 

async def get_image_from_url_3(prompt):


    engine_id = "stable-diffusion-xl-1024-v1-0"
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = os.getenv("STABILITY_API_KEY", SAPI_KEY)

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": prompt,
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        return None

    data = response.json()
    array = []
    for i, image in enumerate(data["artifacts"]):
        res = base64.b64decode(image["base64"])
        if res is None or len(res) == 0:
            continue
        upload_result = upload(res)
        array.append(str(upload_result["url"]))
    return array
        
async def get_image(prompt):
    array = []
    resp1 = await get_image_from_url_1(prompt)
    resp2 = await get_image_from_url_2(prompt)
    resp3 = await get_image_from_url_3(prompt)
    if resp1 is not None:
        array.append(str(resp1))
    if resp2 is not None:
        array.append(str(resp2))
    if resp3 is not None:
        array.extend(resp3)
    return array
   
