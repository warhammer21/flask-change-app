from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

# Set your OpenAI API key directly
api_key = ""

@app.route('/')
def index():
    # Serve the HTML file directly from the current directory
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    try:
        # Make the request to OpenAI API with SSL verification disabled
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4",
                "messages": [
                    {"role": "user", "content": user_input}
                ]
            },
            verify=False  # Disable SSL verification
        )

        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            response_text = result['choices'][0]['message']['content']
            return jsonify({'response': response_text})
        else:
            return jsonify({
                'error': {
                    'status_code': response.status_code,
                    'status_description': response.reason,
                    'content': response.text
                }
            }), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
