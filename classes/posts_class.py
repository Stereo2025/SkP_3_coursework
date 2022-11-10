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
                return f'Ошибка открытия файла {self.save_path}'

            except FileNotFoundError:
                return f'Файл {DATA_PATH} не найден.'

    def get_post_by_user_name(self, name: str) -> list[dict]:
        """Показывает посты по имени пользователя"""

        if not isinstance(name, str):
            raise TypeError("Имя должно быть строковым значением")

        if not name.isalpha():
            raise ValueError("Имя должно содержать только буквы")

        return [post for post in self.load_data() if str(name).lower() == post['poster_name'].lower()]

    def get_post_by_keyword(self, keyword: str) -> list[dict]:
        """Показывает посты по ключевому слову"""

        # if not isinstance(keyword, str):
        #     raise TypeError("Имя должно быть строковым значением")
        #
        # if not keyword:
        #     raise ValueError("Имя должно содержать только буквы")

        return [post for post in self.load_data() if str(keyword).lower() in post['content'].lower().split(' ')]

    def get_post_by_pk(self, pk: int) -> dict:
        """Показывает пост по его pk"""

        # if not isinstance(pk, int):
        #     raise TypeError("Ключ должен быть целым числом")
        #
        # if pk < 0:
        #     raise ValueError("Ключ должен быть положительным числом")

        for post in self.load_data():
            if int(pk) == post['pk']:
                return post

    def get_post_by_tagname(self, tagname: str) -> list[dict]:
        """Показывает посты по тэгнэйму"""

        # if not isinstance(tagname, str):
        #     raise TypeError("Имя должно быть строковым значением")
        #
        # if not tagname.startswith('#'):
        #     raise ValueError("Тэг должен начинаться с #")

        return [tag for tag in self.get_post_by_keyword(tagname) if tagname in tag['content']]

    def view_post(self, post_uid: int) -> dict:
        """Добавляет ссылки на все посты с хэштэг словом"""

        if not isinstance(post_uid, int):
            raise TypeError("Ключ должен быть целым числом")

        if post_uid < 0:
            raise ValueError("Ключ должен быть положительным числом")

        post = self.get_post_by_pk(post_uid)
        result = []

        for word in post["content"].split():
            if word.startswith("#"):
                result.append(f'<a href="/tag/{word[1:]}">{word}</a>')
            else:
                result.append(word)

        post['content'] = ' '.join(result)
        return post
