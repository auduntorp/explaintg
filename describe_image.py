import requests


def describe(filename):
    with open(filename, mode='rb') as image:
        headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': 'f40b6c513c824008b8f9a2a18c85f772'}
        analyze_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=description'
        response = requests.post(analyze_url, data=image, headers=headers)
        return response.json().get('description').get('tags')
    return []

if __name__ == '__main__':
    print(describe('cato-lightning.jpg'))
    