from flask import Flask, request, jsonify
from ragpipeline import rag_query  # Import RAG query function

# Initialize Flask app
app = Flask(__name__)

# Define query endpoint
@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    results = rag_query(user_query)  # Call RAG function
    return jsonify(results.to_dict())

# Only needed for local testing; not used on Vercel
if __name__ == '__main__':
    app.run(debug=True)