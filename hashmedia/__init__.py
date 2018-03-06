from hashstore.utils import load_json_file
from os.path import join, dirname

types = load_json_file(join(dirname(__file__), 'file_types.json'))
