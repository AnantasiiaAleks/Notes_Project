import uuid
from datetime import datetime

NOW = datetime.now()
class Note:
    def __init__(self, note_id=str(uuid.uuid4().int)[:4],
                 date=f'{NOW:%d.%m.%Y %H:%M:%S}',
                 title='title',
                 text='text'):
        self.note_id = note_id
        self.date = date
        self.title = title
        self.text = text

    def get_note_id(self):
        return self.note_id

    def get_date(self):
        return self.date

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def set_note_id(self):
        self.note_id = str(uuid.uuid4().int)[:4]

    def set_date(self):
        self.date = f'{NOW:%d.%m.%Y %H:%M:%S}'

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.text = text

    def to_string(self):
        return self.note_id + ';' + self.title + ';' + self.text + ';' + self.date

    def show_note(self):
        return ('\nID: ' + self.note_id +
                '\nTitle: ' + self.title +
                '\n' + self.text +
                '\nPublication/Edit: ' + self.date)
