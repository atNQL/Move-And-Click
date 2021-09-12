import time
import threading
from pynput.keyboard import Listener, KeyCode
from pynput import keyboard
from pynput.mouse import Button, Controller
from datetime import datetime
import pyautogui


REFRESH_PAGE_TIME = 3

delay = 0.5
button =  Button.left

start_stop_key = keyboard.KeyCode(char='z')

# {keyboard.Key.cmd, keyboard.Key.ctrl}
exit_key = keyboard.Key.esc
# key == keyboard.Key.escz

class btn:
    def __init__(self, btn_position_x, btn_position_y):
        self.x = btn_position_x
        self.y = btn_position_y

class run:
    def __init__(self, refrestPageBtn, crownBtn, refresNumberBtn, bigBtn, smallBtn, moneyInput, okBtn, confirmBtn, informBtn, bigVal, smallVal):
        self.refrestPageBtn = refresNumberBtn
        self.crownBtn = crownBtn
        self.refresNumberBtn = refresNumberBtn
        self.bigBtn = bigBtn
        self.smallBtn = smallBtn
        self.moneyInput = moneyInput
        self.okBtn = okBtn
        self.confirmBtn = confirmBtn
        self.informBtn = informBtn
        self.count = 1
        self.delay = delay
        self.bigVal = bigVal
        self.smallVal = smallVal

    def refreshPage(self):
        pyautogui.moveTo(self.refrestPageBtn.x,self.refrestPageBtn.y, duration = 1)
        mouse.click(button)
        time.sleep(0.5)
        mouse.click(button)
        time.sleep(3)
        pyautogui.moveTo(self.crownBtn.x, self.crownBtn.y, duration = 1)
        mouse.click(button)

        current_time = time.time()
        endtime = current_time + 2
        while current_time < endtime:
            pyautogui.scroll(-10000000)
            current_time = time.time()
        mouse.click(button)
        time.sleep(2)
        pyautogui.moveTo(self.bigBtn.x, self.bigBtn.y, duration = 1)
        current_time = time.time()
        endtime = current_time + 2
        while current_time < endtime:
            pyautogui.scroll(-10000000)
            current_time = time.time()
    
    def click_n_delay(self,x,y, t_delay):
        pyautogui.moveTo(x, y, duration = 1)
        mouse.click(button)
        time.sleep(t_delay)    

    def click_procedure(self,typeBtn,value):
        # move to BIG
        self.click_n_delay(typeBtn.x,typeBtn.y,self.delay)
        # move to INPUT - moneyInput
        self.click_n_delay(self.moneyInput.x,self.moneyInput.y,self.delay)
        pyautogui.typewrite(value)
        time.sleep(1)
        # move to OK - okBtn
        self.click_n_delay(self.okBtn.x,self.okBtn.y,2)
        # move to CONFIRM - confirmBtn
        self.click_n_delay(self.confirmBtn.x,self.confirmBtn.y,1)
        # move to close information - informBtn
        self.click_n_delay(self.informBtn.x,self.informBtn.y,self.delay)

    def start(self):
        if self.count % REFRESH_PAGE_TIME == 0:
            print("Refresh page !")
            self.refreshPage()

        # refresh NUMBER
        self.click_n_delay(self.refresNumberBtn.x,self.refresNumberBtn.y,2)
        # CALL BIG
        self.click_procedure(self.bigBtn, self.bigVal)
        # CALL SMALL
        self.click_procedure(self.smallBtn, self.smallVal)

        self.count = self.count + 1

#   BIG_VAL   = CAP*0.4709
#   SMALL_VAL = CAP*0.5291
# 1 screen
BIG_VAL = "47090"
SMALL_VAL = "52910"
refrestPageBtn = btn(800,105)
crownBtn = btn(60,340)
refresNumberBtn = btn(710,208)
bigBtn = btn(370,365)
smallBtn = btn(580,365)
moneyInput = btn(508,452)
okBtn = btn(706,452)
confirmBtn = btn(356,438)
informBtn = btn(356,350)
runIns = run(refrestPageBtn, crownBtn, refresNumberBtn, bigBtn, smallBtn, moneyInput, okBtn, confirmBtn, informBtn,BIG_VAL,SMALL_VAL)

# 2 screen
BIG_VAL_1 = "2354"
SMALL_VAL_1 = "2645"
refrestPageBtn1 = btn(800,610)
crownBtn1 = btn(60,848)
refresNumberBtn1 = btn(710,719)
bigBtn1 = btn(370,875)
smallBtn1 = btn(580,875)
moneyInput1 = btn(508,958)
okBtn1 = btn(710,958)
confirmBtn1 = btn(356,936)
informBtn1 = btn(356,855)
runIns1 = run(refrestPageBtn1, crownBtn1, refresNumberBtn1, bigBtn1, smallBtn1, moneyInput1, okBtn1, confirmBtn1, informBtn1,BIG_VAL_1,SMALL_VAL_1)

runAll = [runIns, runIns1]


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

                for r in runAll:
                    print("\tRun acc: ", runAll.index(r))
                    r.count = self.count
                    r.start()
                    
                self.count = self.count + 1
                # reset mouse position to prevent unknown action
                pyautogui.moveTo(920, 520, duration = 1)
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
