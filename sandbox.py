
import json
import pathlib

from typing import List, Dict


__HTTP_METHODS = ["POST", "GET", "PUT"]
IN_FILE_PATH: pathlib.Path = "ressources/data/2015-01-01-15.json"


def _load_json_file_to_raws_generator(path: pathlib.Path = IN_FILE_PATH) -> Dict:
    with open(path) as infile:
        for json_line in infile.readlines():
            json_raw = json.loads(json_line)
            yield json_raw


def create_json_status_list(json_raw_generator: _load_json_file_to_raws_generator) -> List:
    return [json_raw for json_raw in json_raw_generator]


status_json_list = create_json_status_list(_load_json_file_to_raws_generator())


print(len(status_json_list))

