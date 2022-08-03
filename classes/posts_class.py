import logging
import json
from json import JSONDecodeError
from global_variables import DATA_PATH


class Posts:

    def __init__(self, save_path=DATA_PATH):
        self.save_path = save_path

    def load_data(self) -> list[dict] | str:
        """Открывает, читает и возвращает все закладки из файла data.json"""

        with open(self.save_path, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)

            except JSONDecodeError:
                logging.info(f'Ошибка открытия файла {self.save_path}')
                return f'Ошибка открытия файла {self.save_path}'

            except FileNotFoundError:
                return f'Файл {DATA_PATH} не найден.'

    def get_post_by_user_name(self, name: str) -> list[dict]:
        """Показывает посты по имени пользователя"""

        return [post for post in self.load_data() if str(name).lower() == post['poster_name'].lower()]

    def get_post_by_keyword(self, keyword: str) -> list[dict]:
        """Показывает посты по ключевому слову"""

        return [post for post in self.load_data() if str(keyword).lower() in post['content'].lower().split(' ')]

    def get_post_by_pk(self, pk: int):
        """Показывает посты по его pk"""

        for post in self.load_data():
            if int(pk) == post['pk']:
                return post

    def get_post_by_tagname(self, tagname: str) -> list[dict]:
        """Показывает посты по тэгнэйму"""

        return [tag for tag in self.load_data() if tagname in tag['content']]

    def view_post(self, post_uid):
        """Добавляет ссылки на все посты с хэштэг словом"""

        post = self.get_post_by_pk(post_uid)
        word = post["content"]
        result = []

        for line in word:
            if line.startswith("#"):
                result.append(f'<a href="/tag/{line[1:]}">{line}</a>')
            else:
                result.append(line)

        post['content'] = ' '.join(result)
        return post
