
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/imagetalk', methods=['POST'])
def create_video_from_talking_photo():
    url = 'https://content.akool.com/api/v1/content/video/createbytalkingphoto'
    headers = {
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1ZTQ0ZTc4MGRlZDMwYzExMDBiNTUyYiIsInVpZCI6MTQ0MjM2NCwidHlwZSI6InVzZXIiLCJmcm9tIjoidG9iIiwiZW1haWwiOiJyYWh1bGphbmdpZDA5eEBnbWFpbC5jb20iLCJmaXJzdE5hbWUiOiJLaW5nIiwiaWF0IjoxNzA5NDY0MjY3LCJleHAiOjE3NDE2MDUwNjd9.LhIVtGW8jx6tVSebvAGxX9PAKllkagySEoaZaN3-ecU'
    }
    data = {
        'talking_photo_url': request.json['talking_photo_url'],
        'input_text': request.json['input_text'],
        'voice_model_id': request.json['voice_model_id']
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        return str(e)

if __name__ == '__main__':
    app.run()
