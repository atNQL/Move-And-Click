from pynput.mouse import Button, Controller
from datetime import datetime
import pyautogui
import random
import winsound
import PIL.ImageGrab
from pynput import keyboard
import time

delay = 1
button =  Button.left

start_stop_key = keyboard.KeyCode(char='z')
exit_key = keyboard.Key.esc

class btn:
    def __init__(self, btn_position_x, btn_position_y, message, rgb_input):
        self.x = btn_position_x
        self.y = btn_position_y
        self.message = message
        self.rgb = rgb_input
class run:
    def __init__(self, refreshPageBtn, crownBtn, refresNumberBtn, bigBtn, smallBtn, moneyInput, okBtn, confirmBtn,confirmBtn_buff, informBtn,menuBtn,recordBtn,rmBtn, confirmRm,cap):
        self.refreshPageBtn = refreshPageBtn
        self.crownBtn = crownBtn
        self.refresNumberBtn = refresNumberBtn
        self.bigBtn = bigBtn
        self.smallBtn = smallBtn
        self.mess = "default"
        self.moneyInput = moneyInput
        self.okBtn = okBtn
        self.confirmBtn = confirmBtn
        self.confirmBtn_buff = confirmBtn_buff
        self.informBtn = informBtn
        self.delay = delay
        self.cap = cap
        self.bigVal = str(round(cap*0.4709))
        self.smallVal = str(round(cap*0.5291))
        self.status = 0
        self.menuBtn = menuBtn
        self.recordBtn = recordBtn
        self.rmBtn = rmBtn
        self.confirmRm = confirmRm

    def setNewCap(self,newValue):
        self.cap = newValue
        self.bigVal = str(round(newValue*0.4709))
        self.smallVal = str(round(newValue*0.5291))
    
    def refreshPage(self):
        pyautogui.moveTo(self.refreshPageBtn.x,self.refreshPageBtn.y, duration = 1)
        mouse.click(button)
        time.sleep(0.5)
        mouse.click(button)
        time.sleep(4)
        pyautogui.moveTo(self.crownBtn.x, self.crownBtn.y, duration = 1)
        time.sleep(1)
        mouse.click(button)

        current_time = time.time()
        endtime = current_time + 2
        while current_time < endtime:
            pyautogui.scroll(-10000000)
            current_time = time.time()
        mouse.click(button)
        mouse.click(button)
        time.sleep(1)
        pyautogui.moveTo(self.bigBtn.x, self.bigBtn.y, duration = 1)
        current_time = time.time()
        endtime = current_time + 1
        while current_time < endtime:
            pyautogui.scroll(-10000000)
            current_time = time.time()
    
    def click_n_delay(self,btn_in, t_delay):
        pyautogui.moveTo(btn_in.x, btn_in.y, duration = 1)
        while pyautogui.position().x != btn_in.x or pyautogui.position().y != btn_in.y:
            self.interrupt("Move to wrong position! >>> STOPPED !")
        
        self.checkRGB(btn_in.x, btn_in.y,btn_in.rgb, btn_in.message)

        mouse.click(button)
        time.sleep(t_delay)

    def removeSubmitted(self):
        print ("Remove summit!")
        pyautogui.moveTo(self.refreshPageBtn.x,self.refreshPageBtn.y, duration = 1)
        mouse.click(button)
        time.sleep(0.5)
        mouse.click(button)
        time.sleep(4)
        self.click_n_delay(self.menuBtn,self.delay)
        self.click_n_delay(self.recordBtn,self.delay)
        time.sleep(7)
        self.click_n_delay(self.rmBtn,self.delay)
        self.click_n_delay(self.confirmRm,self.delay)

    def interrupt(self, mess):
        for i in range(10):
            winsound.Beep(2500,300)
            time.sleep(0.1)

        print("Interrupt at: ", mess)
        if mess == "CEP":
            while True:
                winsound.Beep(2500,5000)
                time.sleep(1)
        if self.status == 1:
            self.removeSubmitted()
        while True:
                winsound.Beep(2500,5000)
                time.sleep(1)

    def checkRGB(self,x, y, rgb_check, mess):
        rgb = PIL.ImageGrab.grab().load()[x,y]
        if rgb != rgb_check:
            self.interrupt(mess, " RGB wrong!")

    def click_procedure(self,typeBtn,value):
        # move to BIG/SMALL
        self.click_n_delay(typeBtn,self.delay)
        if typeBtn.message == "Big":
            self.checkRGB(typeBtn.x,typeBtn.y,(241,49,49), typeBtn.message)
        elif typeBtn.message == "Small":
            self.checkRGB(typeBtn.x,typeBtn.y,(241,49,49), typeBtn.message)

        # move to INPUT - moneyInput
        self.click_n_delay(self.moneyInput,self.delay)

        pyautogui.typewrite(value)
        time.sleep(1)
        rgb = PIL.ImageGrab.grab().load()[self.moneyInput.x,self.moneyInput.y]
        if rgb == self.moneyInput.rgb:
            self.interrupt(" Can not input money!")
        else:
            print("Input",typeBtn.message, ":\tsuccessfully!")    
        # move to OK - okBtn
        self.click_n_delay(self.okBtn,1)
        # move to CONFIRM - confirmBtn
        self.click_n_delay(self.confirmBtn,3)
        self.status = 1
        # move to CONFIRM BUFF - confirmBtn
        # self.click_n_delay(self.confirmBtn_buff.x,self.confirmBtn_buff.y,2)
        # move to close information - informBtn
        rgb = PIL.ImageGrab.grab().load()[self.informBtn.x,self.informBtn.y]
        endtime = time.time() + 5
        while rgb != self.informBtn.rgb:
            print("Over 3s for confirmation form appear!!!")
            current_time = time.time()
            rgb = PIL.ImageGrab.grab().load()[self.informBtn.x,self.informBtn.y]
            if current_time > endtime:
                self.interrupt("CEP")
            time.sleep(0.5)

        self.click_n_delay(self.informBtn,self.delay)

    def start(self):
        # m = random.randint(0,7)
        # if m == 2 or m == 3 or m == 4 or m ==7:
        #     print("\tRefresh page !")
        #     self.refreshPage()

        # refresh NUMBER
        self.click_n_delay(self.refresNumberBtn,2)
    
        rgb = PIL.ImageGrab.grab().load()[self.bigBtn.x,self.bigBtn.y]
        self.checkRGB(self.bigBtn.x,self.bigBtn.y,self.bigBtn.rgb,"First check big")
        rgb = PIL.ImageGrab.grab().load()[self.smallBtn.x,self.smallBtn.y]
        self.checkRGB(self.smallBtn.x,self.smallBtn.y,self.smallBtn.rgb,"First check small")

        n = random.randint(0,1)
        if n == 0 and self.status == 0:
            # CALL BIG - SMALL
            self.click_procedure(self.bigBtn, self.bigVal)
            self.click_procedure(self.smallBtn, self.smallVal)
            self.status = 0
        elif n == 1 and self.status == 0:
            # CALL SMALL - BIG
            self.click_procedure(self.smallBtn, self.smallVal)
            self.click_procedure(self.bigBtn, self.bigVal)
            self.status = 0

mouse = Controller()
