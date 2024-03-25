import uuid
from datetime import datetime


class Note:
    def __init__(self, id = str(uuid.uuid4().int)[:4],
                 date = f'{datetime.now:%d.%m.%Y %H:%M:%S}',
                 title = 'title',
                 text = 'text'):
        self.id = id
        self.date = date
        self.title = title
        self.text = text

    def get_id(self):
        return self.id
    def get_date(self):
        return self.date
    def get_title(self):
        return self.title
    def get_text(self):
        return self.text

    def set_id(self):
        self.id = str(uuid.uuid4().int)[:4]

    def set_date(self):
        self.date = f'{datetime.now:%d.%m.%Y %H:%M:%S}'

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.text=text

    def to_string(self):
        return self.id + ';' + self.title + ';' + self.text + ';' + self.date

    def show_note(self):
        return ('\nID: ' + self.id +
                '\nTitle: ' + self.title +
                '\n' + self.text +
                '\nPublication/Edit: ' + self.date)