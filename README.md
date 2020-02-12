# Keylogger
Send email with logs

## Getting started
Used modules 
- smtplib
- EmailMessage
- pynput

## Description 
This scripts logs all keys pressed until the escape key is pressed. Logs are send as an email to the passed email address.

```python
sender = 'example@gmail.com'  # email that you will use to send logs
password = 'qwerty123'  # password to sender
receiver = 'my@email.com'  # email that you want to receive logs
```
