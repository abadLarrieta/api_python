from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    try:
        
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status() 
        posts = response.json()
        
       
        title_filter = request.args.get('title')
        if title_filter:
            
            posts = [post for post in posts if title_filter.lower() in post['title'].lower()]
        
        return jsonify(posts)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
