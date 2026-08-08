from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        "message": "Hello from your Python Vercel backend!",
        "status": "Success",
        "stack": "Python, Flask, Vercel Serverless"
    })

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    text = data.get('text', '')
    return jsonify({
        "original_text": text,
        "character_count": len(text),
        "word_count": len(text.split())
    })

if __name__ == '__main__':
    app.run(debug=True)