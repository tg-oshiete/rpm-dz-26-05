## Скрин/текст вывода:

    git branch:

```
oshi@oshi-Nitro-AN515-55:~/Projects/VSCode/python/rpm-lessons/26-05$ git branch
  develop
  feature/push
  feature/sms
* main
```

    git log --graph --oneline --all

```
oshi@oshi-Nitro-AN515-55:~/Projects/VSCode/python/rpm-lessons/26-05$ git log --graph --oneline --all
* f8f9626 (HEAD -> main, origin/main) feat: Add SOLID description in README.md
*   b37fdc1 (tag: v1.0.0) merge: develop into main
|\  
| * 1ec04b3 (develop) feat: add message templates
| *   78f1d70 merge: feature/push into develop
| |\  
| | * 2a67636 (feature/push) feat: add Push sender
| |/  
| *   6b07802 merge: feature/sms into develop
| |\  
| | * b9d2502 (feature/sms) feat: add SMS sender
| |/  
| * 80a6e3e feat: add base notifier abstractions and email sender
|/  
* 306621c init: create notification project skeleton
```

## Кратко описать, где именно реализованы 5 принципов SOLID:

S - обязанности разделены между классами. `EmailNotifier`, `SmsSender`, `PushSender` отвечают только за отправку; `EmailValidator`, `SmsValidator`, `PushValidator` - только за проверку контактов; `MessageFormatter` - за форматирование сообщения; `Logger` - за логирование; `MessageTemplateRenderer` - за работу с шаблонами сообщений.

O - для добавления нового способа уведомления не нужно изменять существующие классы отправки. Достаточно создать новый класс, который реализует интерфейс `Notifier`.

L - все отправщики наследуются от `Notifier` и реализуют метод `send()`. Поэтому `EmailNotifier`, `SmsSender` и `PushSender` можно подставлять в `NotificationService` без изменения его кода.

I - интерфейсы разделены. `Notifier` содержит только метод отправки `send()`, а `ContactValidator` содержит только метод проверки контакта `is_valid()`. Отправщики не обязаны заниматься валидацией.

D - `NotificationService` зависит от абстракций `Notifier` и `ContactValidator`, а не от конкретных классов `EmailNotifier`, `SmsSender` или `PushSender`. Конкретные реализации передаются через конструктор.


## Список всех merge-операций:

*   6b07802 merge: feature/sms into develop
*   78f1d70 merge: feature/push into develop
*   b37fdc1 (tag: v1.0.0) merge: develop into main

