# Run server :
# FLASK_APP=app.py flask --debug run

from flask import Flask, request, jsonify
from markupsafe import escape
from errors import RequestError
import service

my_flask = Flask(__name__)
my_flask.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

statuses_json_list = service.load_json_lines_file(service.IN_FILE_PATH)


@my_flask.route("/documents")
def get_github_status():
    if 'page' in request.args:
        print(request.args['page'])
    #return jsonify(statuses_json_list)
    #return model.


@my_flask.route("/documents/<status_id>")
def get_github_status_by_id(status_id):
    return service.get_one_json_status_by_id(escape(status_id), statuses_json_list)

'''
    try:
        asked_status = get_one_json_status_by_id(escape(status_id), _load_json_lines_file(IN_FILE_PATH))
        if not len(asked_status):
            raise RequestError(404)
        return asked_status

    except RequestError as error:
        abort(error.status)

    except:
        abort(422)
'''