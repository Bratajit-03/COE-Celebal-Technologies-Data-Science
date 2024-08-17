from flask import Flask, request, jsonify, render_template
from openai import AzureOpenAI
import os

app = Flask(__name__)

client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  # API key hidden for security reasons
  api_version = "2024-02-01",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prompt = data.get('prompt', '')

    try:
        # Generating the response using the GPT-3.5-Turbo model
        response = client.chat.completions.create(
            engine="gpt-35-turbo",  
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        
        # Extracting the generated text
        generated_text = response['choices'][0]['message']['content']
        return jsonify({'response': generated_text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
