from pynput import mouse
import pyautogui
import time
def on_click(x, y, button, pressed):

    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    pyautogui.press('scrolllock')
    time.sleep(0.3)
    #pyautogui.press('scrolllock')
    # if not pressed:
    #     # Stop listener
    #     return False

# Collect events until released
with mouse.Listener(
               on_click=on_click,
       ) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
       on_click=on_click,)
try:
    listener.start()
except KeyboardInterrupt:
    print("\nExiting...")
