S - обязанности разделены между классами. `EmailNotifier`, `SmsSender`, `PushSender` отвечают только за отправку; `EmailValidator`, `SmsValidator`, `PushValidator` - только за проверку контактов; `MessageFormatter` - за форматирование сообщения; `Logger` - за логирование; `MessageTemplateRenderer` - за работу с шаблонами сообщений.

O - для добавления нового способа уведомления не нужно изменять существующие классы отправки. Достаточно создать новый класс, который реализует интерфейс `Notifier`.

L - все отправщики наследуются от `Notifier` и реализуют метод `send()`. Поэтому `EmailNotifier`, `SmsSender` и `PushSender` можно подставлять в `NotificationService` без изменения его кода.

I - интерфейсы разделены. `Notifier` содержит только метод отправки `send()`, а `ContactValidator` содержит только метод проверки контакта `is_valid()`. Отправщики не обязаны заниматься валидацией.

D - `NotificationService` зависит от абстракций `Notifier` и `ContactValidator`, а не от конкретных классов `EmailNotifier`, `SmsSender` или `PushSender`. Конкретные реализации передаются через конструктор.
