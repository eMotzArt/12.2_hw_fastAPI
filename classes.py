import json
import os.path
import shutil
from datetime import datetime

from globals import UPLOAD_FOLDER


class DataBase:
    """Класс работает с базой данных (сбор, поиск, добавление)"""
    def __init__(self, db_path):
        self.db_path = db_path
        self.db_data = self.get_db_data()

    def get_db_data(self) -> list[dict]:
        """Загружает и возвращает базу"""
        with open(self.db_path, encoding='utf-8') as db_file:
            file_content = json.load(db_file)
        return file_content

    def search_str_in_db_data(self, search_line):
        """Ищет в базе данных совпадающие посты и возвращает их списком"""

        to_return = []
        for item in self.db_data:
            if search_line.lower() in item['content'].lower():
                to_return.append(item)
        return to_return

    def append_new_post_to_db(self, new_post_info):
        """добавляет пост в базу данных"""
        self.db_data.append(new_post_info)
        with open(self.db_path, 'w', encoding='utf-8') as db_file:
            json.dump(self.db_data, db_file, ensure_ascii=False, indent=4)


class NewPostFromRequestData:
    """Класс работает с новым постом (формирует, проверяет, отдает информацию для экспорта в виде словаря, сохраняет файл"""
    def __init__(self, pic, content):
        self.picture = pic
        self.picture_name = self.picture.filename
        self.extension = self.picture.content_type.split('/')[-1]
        self.content = content

        self.pic_full_path = self.generate_file_name()

    def generate_file_name(self):
        """Генерирует путь с именем  файла для сохранения (для уникализации имён)"""

        current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        file_name = f"{current_time}_{self.picture_name}"
        full_path = os.path.join(UPLOAD_FOLDER, file_name)

        return full_path

    def get_info_to_export(self):
        """возвращает подходящий для экспорта словарь"""
        info_to_export = {

            'pic': '\\'+self.pic_full_path,
            'content': self.content
        }

        return info_to_export

    def save_file(self):
        """Сохраняет фотографию"""
        with open(self.pic_full_path, "wb") as save_file:
            shutil.copyfileobj(self.picture.file, save_file)
