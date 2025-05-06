from flask import Flask, request, jsonify
import google.generativeai as genai
import os

APi_Key = os.environ.get("GOOGLE_API_KEY")

if not APi_Key:
    APi_Key="AIzaSyBqm2z_pcTDCU0ubeEMidJRohRkXDvlIsg"

genai.configure(api_key=APi_Key)
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

# Safety settings
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def send_request():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error':'saisir votre demande'}), 400
    try:
        convo = model.start_chat(history=[])
        response = convo.send_message(prompt, generation_config=generation_config, safety_settings=safety_settings)
        return jsonify({'response':response.text})
    except Exception as e:
         return jsonify({'error':str(e)})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




"""_________________________________________________
#------------------------------------------------------------------
#import google.generativeai as genai

genai.configure(api_key="AIzaSyBqm2z_pcTDCU0ubeEMidJRohRkXDvlIsg")

# Initialize the generative model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# Generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

# Safety settings
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

def send_request(prompt):
    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    return convo.last.text


from flask import Flask, request, jsonify
import google.generativeai as genai
import os

api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    api_key = "AIzaSyBqm2z_pcTDCU0ubeEMidJRohRkXDvlIsg"  # **À REMPLACER PAR VOTRE CLÉ API**

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

generation_config = {
   
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Le champ "prompt" est requis.'}), 400

    try:
        convo = model.start_chat(history=[])
        response = convo.send_message(prompt, generation_config=generation_config, safety_settings=safety_settings)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
"""
