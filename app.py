from flask import Flask, render_template, request, jsonify
from db import collection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    required_fields = ['name', 'email', 'title', 'description', 'dueDate']
    if not all(field in data and data[field] for field in required_fields):
        return jsonify({"message": "❌ Please fill in all fields."}), 400
    
    collection.insert_one(data)
    return jsonify({"message": "✅ Task submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)