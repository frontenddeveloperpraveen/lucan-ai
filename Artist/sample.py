#Import all necessary files
import urllib.request
from PIL import Image
import requests
import json
     

#Write description for you
API_URL = "https://api-inference.huggingface.co/models/Gustavosta/MagicPrompt-Stable-Diffusion"
headers = {"Authorization": "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"}  #Replace entire  with your api token. You can get from https://huggingface.co/

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Rabit with carrot in forest ",
})

print(output)
magicPrompt=output[0].get('generated_text')
output


     

#Generates the image using Lightning.Ai muse api
response = requests.post("https://yzgqm-01gxvcx76jm5e363j6fbc7zz4a.litng-ai-03.litng.ai/api/predict", json={
  "prompt": magicPrompt,
  "high_quality": "false"
})
     

imgUrl = response.json()['image']

urllib.request.urlretrieve(
  imgUrl,
   "Ai.png")
  
img = Image.open("Ai.png")
img.save()