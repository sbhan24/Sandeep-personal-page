# server.py
from flask import Flask, request, jsonify
import openai
import os
openai.api_key = "sk-None-rin8j3sDHwE73MdNDjniT3BlbkFJTJGhfvnLBCU1NV7OCC4B"
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure OPENAI_API_KEY is set in your environment

app = Flask(__name__)

@app.route('/api/upload-pdfs', methods=['POST'])
def upload_pdfs():
    files = request.files.getlist("pdf-files")
    # Implement your PDF processing logic here (e.g., extract text, save files)
    # For now, we'll return a simple response.
    return jsonify({"status": "PDFs uploaded successfully!"}), 200

@app.route('/api/chatgpt', methods=['POST'])
def chatgpt():
    data = request.get_json()
    question = data.get("question")

    # Send the question to OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    
    answer = response['choices'][0]['message']['content']
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(port=5000)
