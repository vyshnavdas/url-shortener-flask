from flask import Flask, jsonify, redirect, request
from pymongo import MongoClient
import string, random
from config import DB_URL

app = Flask(__name__)
client = MongoClient(DB_URL)
db = client['url_shortener']
collection = db['urls']

@app.route('/shorten', methods=['GET'])
def shorten_url():
    if request.headers.get('Content-Type') == 'application/json':
        long_url = request.json.get('long_url')
    else:
        long_url = request.args.get('long_url')


    short_code = generate_short_code()

    collection.insert_one({'short_code': short_code, 'long_url': long_url})

    shortened_url = request.host_url + short_code
    return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    result = collection.find_one({'short_code': short_code})

    if result:
        long_url = result['long_url']
        return redirect(long_url, code=302)
    else:
        return jsonify({'error': 'URL not found'}), 404

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

if __name__ == '__main__':
    app.run()