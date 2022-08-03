import json
from json import JSONDecodeError
from global_variables import BOOKMARKS_PATH


class BookMarks:

    def __init__(self, save_path=BOOKMARKS_PATH):
        self.save_path = save_path

    def load_bookmarks(self) -> list[dict] | str:
        """Открывает, читает и возвращает все закладки из файла bookmarks.json"""

        with open(self.save_path, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)

            except JSONDecodeError:
                return f'Ошибка открытия файла {self.save_path}.'

            except FileNotFoundError:
                return f'Файл {BOOKMARKS_PATH} не найден.'

    def add_bookmarks(self, uid):
        """Добалвяет закладку в файл bookmarks.json"""

        add_bookmark = self.load_bookmarks()
        # Если id уже есть в файле или id 'некорректный' функция прекратит свою работу и дальнейший
        # блок выполняться не будет. Иначе выполниться блок с добавлением закладки в файл.
        if uid in add_bookmark or not uid:
            return

        add_bookmark.append(uid)
        with open(self.save_path, 'w', encoding='utf-8') as file:
            json.dump(add_bookmark, file, indent=2, ensure_ascii=False)

    def delete_bookmarks(self, uid):
        """Удаляет закладку из файла bookmarks.json"""

        del_bookmark = self.load_bookmarks()
        # Если id в файле нет, или он некорректный выполнится ветка if. Иначе else.
        if uid not in del_bookmark or not uid:
            return

        del_bookmark.remove(uid)
        with open(self.save_path, 'w', encoding='utf-8') as file:
            json.dump(del_bookmark, file, indent=2, ensure_ascii=False)
