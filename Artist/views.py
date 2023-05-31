from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
import requests
from .models import Prompt
def Home(request):
    return render(request,'html/lucan.html')

def Redirect(request,name):
    return redirect('/playground')

def Imagine(request):
    print('Ok')
    request_text = request.body.decode('utf-8')
    data = json.loads(request_text)
    print(data)
    positive_prompt = data.get('prompt')
    negative_prompt = data.get('nprompt')
    print(positive_prompt, negative_prompt)
    add = Prompt.objects.create(positive=positive_prompt,negative=negative_prompt)
    add.save()
    url = "https://stablediffusionapi.com/api/v3/text2img"
    payload = json.dumps({
    "key": "TLvAa96JNWM7pYguVtU9MXbzhD3Wa8yWob1dvifV5yoLHQxTjiUB0gbzM7Px",
    "prompt": positive_prompt,
    "negative_prompt": negative_prompt,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": "embeddings_model_id",
    "webhook": None,
    "track_id": None
    })

    headers = {
    'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

        response_data = json.loads(response.text)

        link = response_data['output']

        return JsonResponse({'link':link,'msg':'success'})
    except Exception as e:
        return JsonResponse({'link':'https://images.pexels.com/photos/2882552/pexels-photo-2882552.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1.png','msg':'error','intimation':str(e)})