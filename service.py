import pathlib
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from typing import Dict, List
import model
import json
import copy

# connects to DB
__DB_NAME = 'github_status.db'
engine = create_engine('sqlite:///' + __DB_NAME, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

IN_FILE_PATH: pathlib.Path = "ressources/data/2015-01-01-15.json"


def load_json_lines_file(path: pathlib.Path) -> List[Dict]:
    with open(path) as infile:
        return [convert_to_dict_of_str(json.loads(json_line)) for json_line in infile.readlines()]


def convert_to_dict_of_str(status_to_convert: Dict) -> Dict:
    converted_status = {}
    for key in status_to_convert.keys():
        converted_status[key] = str(status_to_convert[key])
    return converted_status


def get_one_json_status_by_id(status_id: int, json_raws: load_json_lines_file) -> Dict:
    status_with_id = {}
    for json_status in json_raws:
        if status_id == json_status['id']:
            status_with_id = json_status
            break
    return status_with_id


def add_status(data: Dict):
    # Adding objects
    session = Session()
    new_status = model.Status(**data)
    session.add(new_status)
    session.commit()


def get_statuses():
    # Querying
    session = Session()
    for status in session.query(model.Status).order_by(model.Status.id):
        print(status)


statuses_json_list = load_json_lines_file(IN_FILE_PATH)
# datas = [{'id': 'momo', 'actor': 'omom'}, {'id': 'david', 'actor': 'divad'}]
for status in statuses_json_list:
    print(type(status))
    add_status(status)

'''responses = get_statuses()
print(responses)'''
