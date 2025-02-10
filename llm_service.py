import requests
import json
def generate_text(prompt):
    print("prompt:{}".format(prompt))
    try:
        payload = {
                "model" : "mistral",
                "prompt" : f"summarize the text inside square brackets not more than 10 words [{prompt}]",
                "stream" : False
            }
        api_url = "http://localhost:11434/api/generate"
        response = requests.post(api_url, json=payload)
        if response.status_code ==200:
            responses = response.content.split(b'\n')
            generate_text = ''
            for obj in responses:
                if obj:
                    response_data = json.loads(obj.decode())
                    response= response_data.get("response")
                    if response:
                        if response.strip():
                            if response == " ":
                                generate_text += response
                            else:
                                if generate_text:
                                    generate_text += ' '
                                generate_text += response.strip()
            print(generate_text)
            return generate_text
        else:
            print(f"Error: Failed to generate text. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")


