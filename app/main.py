from flask import Flask, request, render_template, jsonify
from openai import OpenAI
from db.connector import log_chat, fetch_chat_history

client = OpenAI()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = call_chatgpt(prompt)
        return render_template('index.html', response=response, prompt=prompt)
    return render_template('index.html', response=None)

def call_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be pretend as a warm boyfriend, and your task is to comfort your upset girlfriend."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    log_chat(prompt, response.choices[0].message.content)
    return response.choices[0].message.content

@app.route('/history', methods=['GET'])
def history():
    records = fetch_chat_history()
    return jsonify({"chat_history": records})

@app.route('/about')
def about():
    return 'A simple ChatGPT wrapper application.'

if __name__ == '__main__':
    app.run(debug=True)
