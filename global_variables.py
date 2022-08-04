from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.joinpath('json_lists', 'data.json')
COMMENTS_PATH = BASE_DIR.joinpath('json_lists', 'comments.json')
BOOKMARKS_PATH = BASE_DIR.joinpath('json_lists', 'bookmarks.json')
PATH_LOGS_CONFIG = BASE_DIR.joinpath('logs', 'config.log')
PATH_MAIN_LOGS = BASE_DIR.joinpath('logs', 'main.log')
