import pygame as pg

def init():
    pg.init()
    win = pg.display .set_mode((40,40))

def getKey(keyName):
    result = False
    for events in pg.event.get(): pass
    keyInput = pg.key.get_pressed()
    myKey = getattr(pg, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        result = True
    pg.display.update()
    return result

def main():
    print(getKey("s"))



if __name__ == '__main__':
    init()
    while True:
        main()
# from pynput import keyboard
# import time
#
# class KeyMonitor:
#     def __init__(self):
#         self.keys = set()
#         self.listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)
#         self.listener.start()
#
#     def _on_press(self, key):
#         self.keys.add(str(key))
#
#     def _on_release(self, key):
#         self.keys.discard(str(key))
#
#     def getKey(self, key_name):
#         return '\'' + key_name + '\'' in self.keys
#
# # Init function that returns a KeyMonitor instance
# def init():
#     return KeyMonitor()
#
# def main():
#     km = KeyMonitor()
#     while True:
#         print(km.getKey("s"))
#         time.sleep(0.1)
#
# if __name__ == '__main__':
#     main()
