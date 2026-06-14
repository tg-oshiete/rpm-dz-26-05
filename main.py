from abc import ABC, abstractmethod
from datetime import datetime



class Notifier(ABC):
    @abstractmethod
    def send(self, message: str, to: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str, to: str):
        print(f"Отправлено email сообщение:[{message}] на устройство: {to}")


class SmsSender(Notifier):
    def send(self, message: str, to: str):
        print(f"Отправлено SMS сообщение:[{message}] на устройство: {to}")


class PushSender(Notifier):
    def send(self, message: str, to: str):
        print(f"Отправлено PUSH уведомление:[{message}] на устройство: {to}")


class ContactValidator(ABC):
    @abstractmethod
    def is_valid(self, contact: str) -> bool:
        pass


class EmailValidator(ContactValidator):
    def is_valid(self, contact: str) -> bool:
        return "@" in contact and "." in contact


class SmsValidator(ContactValidator):
    def is_valid(self, contact: str) -> bool:
        return "+" in contact and contact[1:].isdigit()


class PushValidator(ContactValidator):
    def is_valid(self, contact: str) -> bool:
        return contact.isdigit()


class MessageFormatter:
    def format(self, title: str, text: str) -> str:
        return f"[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {title}: {text}"
    

class Logger:
    def log(self, message: str):
        print(f"[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {message}")
    

class NotificationService:
    def __init__(self, notifier: Notifier, formatter: MessageFormatter, logger: Logger, validator: ContactValidator):
        self.notifier = notifier
        self.formatter = formatter
        self.logger = logger
        self.validator = validator

    def notify(self, title: str, text: str, to: str):
        if not self.validator.is_valid(to):
            self.logger.log(f"[LOG] Не пройдена валидация контакта: [{to}]")
            return

        message = self.formatter.format(title, text)
        self.notifier.send(message, to)
        self.logger.log(f"[LOG] Уведомление отправлено: [{to}]")


class MessageTemplateRenderer:
    def __init__(self):
        self.templates = {
            "registration": "{name}, вы успешно зарегистрировались.",
            "login": "{name}, вы успешно авторизовались.",
            "notifications": "{title}\n{text}"
        }
    
    def render(self, template: str, **kwargs):
        if template not in self.templates:
            raise ValueError(f"Шаблон {template} не найден")
        
        return self.templates[template].format(**kwargs)

def main():
    notifier = EmailNotifier()
    formatter = MessageFormatter()
    logger = Logger()
    validator = EmailValidator()
    service = NotificationService(notifier=notifier, formatter=formatter, logger=logger, validator=validator)
    
    renderer = MessageTemplateRenderer()
    
    message = renderer.render(
        "registration",
        name="Oleg"
    )

    if validator.is_valid("user@example.com"):
        notifier.send(message, "user@example.com")
        logger.log("Уведомление отправлено")
    else:
        logger.log("Ошибка: неверный email")
    
    service.notify(title="Заголовок", text="Текст сообщения", to="example@gmail.com")

    sms_notifier = SmsSender()
    sms_validator = SmsValidator()
    sms_service = NotificationService(notifier=sms_notifier, formatter=formatter, logger=logger, validator=sms_validator)
    sms_service.notify(title="Заголовок", text="Текст сообщения", to="+73827592")


    push_notifier = PushSender()
    push_validator = PushValidator()
    push_service = NotificationService(notifier=push_notifier, formatter=formatter, logger=logger, validator=push_validator)
    push_service.notify(title="Заголовок", text="Текст сообщения", to="128481239")

if __name__ == "__main__":
    main()