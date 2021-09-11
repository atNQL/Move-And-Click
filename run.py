import time
import threading
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller
from datetime import datetime
import pyautogui

class btn:
    def __init__(self, btn_position_x, btn_position_y):
        self.x = btn_position_x
        self.y = btn_position_y

REFRESH_PAGE_TIME = 3

# 1 screen
refrestPageBtn = btn(995,187)
crownBtn = btn(96,483)
refresNumberBtn = btn(887,315)
bigBtn = btn(451,515)
smallBtn = btn(790,515)
moneyInput = btn(650,620)
okBtn = btn(907,620)
confirmBtn = btn(465,590)
informBtn = btn(465,500)
# 2 screen
# refrestPageBtn = btn(4530,210)
# crownBtn = btn(2725,800)
# refresNumberBtn = btn(4315,480)
# bigBtn = btn(3471,865)
# smallBtn = btn(3900, 880)
# moneyInput = btn(3790, 1070)
# okBtn = btn(4308, 1070)
# confirmBtn = btn(3471, 1010)
# informBtn = btn(3471, 800)

delay = 0.5
button =  Button.left

start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.count = 1
        

    def start_clicking(self):
        self.running = True
        print("Start autoclick now\n")

    def stop_clicking(self):
        self.running = False
        print("Stop autoclick now")

    def exit(self):
        self.stop_clicking()
        self.program_running  = False

    def refreshPage(self):
        pyautogui.moveTo(refrestPageBtn.x,refrestPageBtn.y, duration = 1)
        mouse.click(button)
        time.sleep(0.5)
        mouse.click(button)
        time.sleep(3)
        pyautogui.moveTo(crownBtn.x, crownBtn.y, duration = 1)
        mouse.click(button)

        current_time = time.time()
        endtime = current_time + 2
        while current_time < endtime:
            pyautogui.scroll(-10000000)
            current_time = time.time()
        mouse.click(button)
        time.sleep(2)
        pyautogui.moveTo(bigBtn.x, bigBtn.y, duration = 1)
        current_time = time.time()
        endtime = current_time + 2
        while current_time < endtime:
            pyautogui.scroll(-10000000)
            current_time = time.time()
    
    def click_n_delay(self,x,y, t_delay):
        pyautogui.moveTo(x, y, duration = 1)
        mouse.click(self.button)
        time.sleep(t_delay)    

    def click_procedure(self,typeBtn,value):
        # move to BIG
        self.click_n_delay(typeBtn.x,typeBtn.y,self.delay)
        # move to INPUT - moneyInput
        self.click_n_delay(moneyInput.x,moneyInput.y,self.delay)
        pyautogui.typewrite(value)
        time.sleep(1)
        # move to OK - okBtn
        self.click_n_delay(okBtn.x,okBtn.y,2)
        # move to CONFIRM - confirmBtn
        self.click_n_delay(confirmBtn.x,confirmBtn.y,1)
        # move to close information - informBtn
        self.click_n_delay(informBtn.x,informBtn.y,self.delay)
    
    def run(self):
        while self.program_running:
            while self.running:
                print("Time  ------- ", self.count)
                time.sleep(1)
                print("...3")
                time.sleep(1)
                print("...2")
                time.sleep(1)
                print("...1")
                time.sleep(1)
                print("...0")
                print(time.strftime('%X %x %Z'))
                if self.count % REFRESH_PAGE_TIME == 0:
                    print("Refresh page !")
                    self.refreshPage()
                
                # refresh NUMBER
                self.click_n_delay(refresNumberBtn.x,refresNumberBtn.y,2)
                # CALL BIG
                self.click_procedure(bigBtn, "16481")
                # CALL SMALL
                self.click_procedure(smallBtn, "18518")

                self.count = self.count + 1
                # reset mouse position to prevent unknown action
                pyautogui.moveTo(156, 900, duration = 1)
                if self.count % REFRESH_PAGE_TIME == 1:
                    time.sleep(256)
                else:
                    time.sleep(269)

mouse = Controller()
click_thread =  ClickMouse(delay,button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        print("END!")
        exit()

with Listener(on_press = on_press) as listener:
    print("READY!")
    listener.join()
