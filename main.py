from abc import ABC, abstractmethod
from datetime import datetime



class Notifier(ABC):
    @abstractmethod
    def send(self, message: str, to: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str, to: str):
        print(f"Отправлено email сообщение:[{message}] на устройство: {to}")


class ContactValidator(ABC):
    @abstractmethod
    def is_valid(self, contact: str) -> bool:
        pass


class EmailValidator(ContactValidator):
    def is_valid(self, contact: str) -> bool:
        return "@" in contact and "." in contact


class MessageFormatter:
    def format(self, title: str, text: str) -> str:
        return f"[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {title}: {text}"
    

class Logger:
    def log(self, message: str):
        return f"[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {message}"
    

class NotificationService:
    def __init__(self, notifier: Notifier, formatter: MessageFormatter, logger: Logger, validator: ContactValidator):
        self.notifier = notifier
        self.formatter = formatter
        self.logger = logger
        self.validator = validator

    def notify(self, title: str, text: str, to: str):
        if not self.validator.is_valid(to):
            self.looger.log(f"[LOG] Не пройдена валидация контакта: [{to}]")

        message = self.formatter.format(title, text)
        self.notifier.send(message, to)
        self.logger.log(f"[LOG] Уведомление отправлено: [{to}]")


def main():
    notifier = EmailNotifier()
    formatter = MessageFormatter()
    logger = Logger()
    validator = EmailValidator()
    service = NotificationService(notifier=notifier, formatter=formatter, logger=logger, validator=validator)

    service.notify(title="Заголовок", text="Текст сообщения", to="example@gmail.com")

if __name__ == "__main__":
    main()