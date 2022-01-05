
import os

from dotenv import load_dotenv

from flask import Flask
from flask import request
from flask import jsonify
from werkzeug.exceptions import BadRequestKeyError

from deta import Deta

load_dotenv()

NUMBER_CPU = 2


app = Flask(__name__)
db = Deta(os.environ['KEY']).Base(os.environ['NAME_DB'])


@app.route('/v1/urls', methods=['GET'])
def get_data():
    try:
        if request.args['key']:
            return db.get(request.args['key']) or jsonify({'error': 'Not found'})
    except BadRequestKeyError:
        return jsonify({'error': 'bad request'})


@app.route('/v1/urls', methods=['POST'])
def put_data():
    try:
        url = request.get_json()['url']
        if request.get_json()['status_url'] in ['need_to_check', 'processed']:
            status_url = request.get_json()['status_url']
        if request.get_json()['number_CPU'] <= NUMBER_CPU:
            number_CPU = request.get_json()['number_CPU']
    except KeyError:
        return jsonify({'error': 'bad request'})

    data = {
        'key': url,
        'url': url,
        'status_url': status_url,
        'number_CPU': number_CPU,
            }
    db.put(data, key=url)
    return jsonify({'success': 'record created or updated'})


@app.route('/v1/urls', methods=['DELETE'])
def delete_data():
    try:
        db.delete(request.args['key'])
        return jsonify({'success': 'record deleted'})
    except BadRequestKeyError:
        return jsonify({'error': 'bad request'})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
