import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Load API key from environment or configuration file
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_content(prompt, model="text-davinci-003", max_tokens=150):
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

@app.route("/generate", methods=["POST"])
def generate():
    content = request.json
    prompt = content.get("prompt")
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    generated_text = generate_content(prompt)
    return jsonify({"result": generated_text})

if __name__ == "__main__":
    app.run(debug=True)
