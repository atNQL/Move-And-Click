import pyautogui, sys
import PIL.ImageGrab
print('Press Ctrl-C to quit.')

try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        if x <= 1920 and y <= 1080: 
            rgb = PIL.ImageGrab.grab().load()[x,y]
            positionStr = positionStr + ' rgb:' + str(rgb) 
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\n')