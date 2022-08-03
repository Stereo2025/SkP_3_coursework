import json
from json import JSONDecodeError
from global_variables import COMMENTS_PATH


class Comments:

    def __init__(self, save_path=COMMENTS_PATH):
        self.save_path = save_path

    def load_comments(self) -> list[dict] | str:
        """Открывает, читает и возвращает все закладки из файла comments.json"""

        with open(self.save_path, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)

            except JSONDecodeError:
                return f'Ошибка открытия файла {self.save_path}'

            except FileNotFoundError:
                return f'Файл {COMMENTS_PATH} не найден.'

    def get_some_comment(self, post_id: int) -> list[dict]:
        """Возвращает комментарий по его id"""

        return [uid for uid in self.load_comments() if int(post_id) == uid['post_id']]
