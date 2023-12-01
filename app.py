from flask import Flask, render_template, request
import openai
import os 
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
openai.api_type = "azure"
openai.api_base = "https://reliasopenaitesting.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    message_text = [
        {"role":"system","content":"You are an AI assistant that helps people find information."},
        {"role":"user","content": userText}
    ]
    completion = openai.ChatCompletion.create(
        engine="ChatGPT4LargeRelias",
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    result = completion.choices[0].message['content']
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8002,debug=True)
