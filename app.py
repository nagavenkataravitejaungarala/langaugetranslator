from flask import Flask, send_from_directory, request, jsonify
import requests

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    api_key = data.get('api_key')
    from_lang = data.get('from_lang')
    to_lang = data.get('to_lang')
    text = data.get('text')

    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
    payload = {
        "from": from_lang,
        "to": to_lang,
        "q": text
    }
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "rapid-translate-multi-traduction.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Translation failed", "status_code": response.status_code, "message": response.text})

if __name__ == '__main__':
    app.run(debug=True)
