from Message.MessageStorage import *
from Message.message import *


class FileMessageStorage(AbstractMessageStorage):
    def __init__(self, file: Path, delimiter=']['):
        self._path = file
        self._delimiter = delimiter

        if not self._path.exists:
            self._path.open('w')

    def get_all(self) -> Iterable[Message]:
        try:
            with self._path.open('r') as f:
                for line in f.readlines():
                    values = line.split('][')
                    yield Message(datetime.strptime(values[0], "%Y-%m-%d %H:%M:%S.%f"), values[1],
                                  values[2].removesuffix('\n'))

        except FileNotFoundError:
            pass

#   Преобразует строку из файла в объект Message
    def message_maker(self, line: str) -> Message:
        datetime_formatter: str = "%Y-%m-%d %H:%M:%S.%f"
        __mg_time_str, login, message = line.split('][')
        __mg_time = datetime.strptime(__mg_time_str, datetime_formatter)
        return Message(__mg_time, login, message)

#   Преобразует Message в строку
    def _make_line(self, message: Message) -> str:
        return self._delimiter.join([str(message.mg_time), message.login, message.message])

#   Добавляет строку в файл
    def put_one(self, message: Message):
        lines = [self._make_line(x) for x in self.get_all() if x.mg_time != message.mg_time] + [self._make_line(message)]
        self._path.write_text('\n'.join(lines))

#   Считывает строки из файла и перезаписывает в файл, если message.time не равен искомому
    def delete_one(self, mg_time: datetime):
        lines = [self._make_line(message) for message in self.get_all() if message.mg_time != mg_time]
        self._path.write_text('\n'.join(lines))


