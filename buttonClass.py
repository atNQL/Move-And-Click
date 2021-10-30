from pynput.mouse import Button, Controller
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
waitingClickTime=[2,0,3,4,7,1]


class btn:
    def __init__(self, btn_position_x, btn_position_y, message, rgb_input):
        self.x = btn_position_x
        self.y = btn_position_y
        self.message = message
        self.rgb = rgb_input
class run:
    def __init__(self, x_base, y_base, cap):
        self.refreshPageBtn = btn(x_base + 785,y_base + 94,"Refresh Page" ,(0,0,0))
        self.crownBtn = btn(x_base + 45,y_base + 347,"Crown btn",(241,49,49))
        self.refresNumberBtn = btn(x_base + 695,y_base + 203,"F5 Number",(239, 141, 134))
        self.bigBtn = btn(x_base + 447,y_base + 370,"Big", (255,255,255)) #btn(416,875,())
        self.smallBtn = btn(x_base + 798,y_base + 372,"Small",(255,255,255)) #btn(626,875)
        self.moneyInput = btn(x_base + 486,y_base + 441,"Money Input",(175,175,175))
        self.okBtn = btn(x_base + 695,y_base + 442,"Ok",(241, 49, 49))
        self.confirmBtn = btn(x_base + 346,y_base + 419,"Submit",(255, 0, 0))
        self.selfCheckBtn = btn(x_base + 547,y_base + 360,"Self Check",(65, 35, 242))
        self.informBtn = btn(x_base + 388,y_base + 345,"Confirm",(0, 122, 255))
        self.menuBtn = btn(x_base + 788,y_base + 142,"Menu",(242,64,64))
        self.recordBtn = btn(x_base + 730,y_base + 293,"Record btn",(252,252,252))
        self.removeLastOderBtn = btn(x_base + 568,y_base + 244,"Remove btn",(78,162,255))

        self.removePenultimateOrderBtn = btn(x_base + 567,y_base + 328,"Remove btn",(173,212,255))

        self.confirmRm = btn(x_base + 458,y_base + 366,"Confirm Remove btn",(250,250,250))
        self.lastCheck = btn(x_base + 370,y_base + 346,"Confirm Remove btn",(80,80,80))
        self.smallCheck = btn(x_base + 444,y_base + 371,"Small order check",(150, 150, 150))
        self.bigCheck = btn(x_base + 444,y_base + 371,"Big ordder Check",(174, 174, 174))
        self.iconCheck = btn(x_base + 206,y_base + 199,"Icon Check",(91,154,223))
        self.backBtn = btn(x_base + 186,y_base + 141,"Back record btn", (241,49,49))
        self.excuseRefreshPage = btn(x_base + 48,y_base + 249,"Back record btn", (241,49,49))
        self.delay = delay
        self.mess = "default"
        self.cap = cap
        self.bigVal = str(round(cap*0.4709))
        self.smallVal = str(round(cap*0.5291))
        self.status = 0
        self.profit = 0
        self.profitBound = 100

    def calProfitNewCap(self):
        self.profit = self.profit + round(self.cap*0.000736) 
        if self.profit >= self.profitBound:
            self.cap = self.cap + self.profitBound
            self.bigVal = str(round(self.cap*0.4709))
            self.smallVal = str(round(self.cap*0.5291))
            self.profit = self.profit - self.profitBound
            print ("Next cap is ", self.cap)
        
    
    def refreshPage(self):
        pyautogui.moveTo(self.refreshPageBtn.x,self.refreshPageBtn.y, duration = 0.5)
        mouse.click(button)
        time.sleep(0.5)
        mouse.click(button)
        
        rgb = PIL.ImageGrab.grab().load()[self.excuseRefreshPage.x,self.excuseRefreshPage.y]
        endtime = time.time() + 10
        while rgb != self.okBtn.rgb:
            print("\t--> Waiting for loading page!!!")
            current_time = time.time()
            rgb = PIL.ImageGrab.grab().load()[self.excuseRefreshPage.x,self.excuseRefreshPage.y]
            if current_time > endtime:
                self.interrupt("Can not load page!!!")
            time.sleep(1)


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
        time.sleep(0.5)
        pyautogui.moveTo(self.bigBtn.x, self.bigBtn.y, duration = 1)
        current_time = time.time()
        endtime = current_time + 1
        while current_time < endtime:
            pyautogui.scroll(-10000000)
            current_time = time.time()
    
    def click_n_delay(self,btn_in, t_delay):
        pyautogui.moveTo(btn_in.x, btn_in.y, duration = 0.5)
        while pyautogui.position().x != btn_in.x or pyautogui.position().y != btn_in.y:
            self.interrupt("Move to wrong position! >>> STOPPED !")
        
        self.checkRGB(btn_in.x, btn_in.y,btn_in.rgb, btn_in.message)

        mouse.click(button)
        time.sleep(t_delay)

    def removeSubmitted(self):
        print ("Remove summit!")

        # pyautogui.moveTo(self.refreshPageBtn.x,self.refreshPageBtn.y, duration = 1)
        # mouse.click(button)
        # time.sleep(0.5)
        # mouse.click(button)
        # time.sleep(4)
        # self.click_n_delay(self.menuBtn,self.delay)
        # self.click_n_delay(self.recordBtn,self.delay)
        # time.sleep(7)
        # self.click_n_delay(self.removeBtn,self.delay)
        # self.click_n_delay(self.confirmRm,self.delay)

    def interrupt(self, mess):
        print("Interrupt at: ", mess)
        for i in range(10):
            winsound.Beep(2500,300)
            time.sleep(0.1)
        
        if mess == "CEP":
            while True:
                winsound.Beep(2500,3000)
                time.sleep(1)
        if self.status == 1:
            self.removeSubmitted()
        while True:
                winsound.Beep(2500,3000)
                time.sleep(1)

    def checkOrder(self):
        self.click_n_delay(self.menuBtn,self.delay)
        time.sleep(0.7)
        self.click_n_delay(self.recordBtn,self.delay)
        # default wait time
        time.sleep(2)
        # extern wait time
        rgb = PIL.ImageGrab.grab().load()[self.removeLastOderBtn.x,self.removeLastOderBtn.y]
        endtime = time.time() + 7
        while rgb != self.removeLastOderBtn.rgb:
            print("\t--> Waiting for loading all order!!!")
            current_time = time.time()
            rgb = PIL.ImageGrab.grab().load()[self.removeLastOderBtn.x,self.removeLastOderBtn.y]
            if current_time > endtime:
                self.interrupt("Can not check all order!!!")
            time.sleep(1)
        
        # check 2 order exist
        self.checkRGB(self.removeLastOderBtn.x,self.removeLastOderBtn.y,self.removeLastOderBtn.rgb, "Check Big order exist 2 order or not!")
        self.checkRGB(self.removePenultimateOrderBtn.x,self.removePenultimateOrderBtn.y,self.removePenultimateOrderBtn.rgb, "Check Small exist 2 order or not!")

        pyautogui.moveTo(self.removeLastOderBtn.x - 200, self.removeLastOderBtn.y + 85, duration = 1)
        mouse.click(button)
        rgb = PIL.ImageGrab.grab().load()[self.iconCheck.x,self.iconCheck.y]
        endtime = time.time() + 10
        while rgb != self.iconCheck.rgb:
            print("\t--> Waiting for loading small order!!!")
            current_time = time.time()
            rgb = PIL.ImageGrab.grab().load()[self.iconCheck.x,self.iconCheck.y]
            if current_time > endtime:
                self.interrupt("Can not load small order!!!")
            time.sleep(1)

        self.checkRGB(self.smallCheck.x, self.smallCheck.y,self.smallCheck.rgb,self.smallCheck.message)

        self.click_n_delay(self.backBtn,self.delay)
        rgb = PIL.ImageGrab.grab().load()[self.removeLastOderBtn.x,self.removeLastOderBtn.y]
        endtime = time.time() + 10
        while rgb != self.removeLastOderBtn.rgb:
            print("\t--> Waiting for loading all order!!!")
            current_time = time.time()
            rgb = PIL.ImageGrab.grab().load()[self.removeLastOderBtn.x,self.removeLastOderBtn.y]
            if current_time > endtime:
                self.interrupt("Can not check all order!!!")
            time.sleep(1)

        pyautogui.moveTo(self.removeLastOderBtn.x-200, self.removeLastOderBtn.y, duration = 0.5)
        mouse.click(button)
        rgb = PIL.ImageGrab.grab().load()[self.iconCheck.x,self.iconCheck.y]
        endtime = time.time() + 10
        while rgb != self.iconCheck.rgb:
            print("\t--> Waiting for loading big order!!!")
            current_time = time.time()
            rgb = PIL.ImageGrab.grab().load()[self.iconCheck.x,self.iconCheck.y]
            if current_time > endtime:
                self.interrupt("Can not load big order!!!")
            time.sleep(1)

        self.checkRGB(self.bigCheck.x, self.bigCheck.y,self.bigCheck.rgb,self.bigCheck.message)


        print("Back to main page!!!")
        self.click_n_delay(self.backBtn,self.delay)
        self.click_n_delay(self.backBtn,self.delay)
        
        # time.sleep(7)
        # self.click_n_delay(self.removeBtn,self.delay)
        # self.click_n_delay(self.confirmRm,self.delay)

    def checkRGB(self,x, y, rgb_check, mess):
        rgb = PIL.ImageGrab.grab().load()[x,y]
        if rgb != rgb_check:
            mess = mess + " RGB wrong!"
            self.interrupt(mess)

    def click_procedure(self,typeBtn,value):
        if typeBtn.message == "Big":
            self.checkRGB(self.smallBtn.x,self.smallBtn.y,self.smallBtn.rgb,"Second check small")
        elif typeBtn.message == "Small":
            self.checkRGB(self.bigBtn.x,self.bigBtn.y,self.bigBtn.rgb,"Second check big")
        
        # move to BIG/SMALL
        self.click_n_delay(typeBtn,self.delay)
        self.checkRGB(typeBtn.x,typeBtn.y,(241,49,49), typeBtn.message)

        # move to INPUT - moneyInput
        self.click_n_delay(self.moneyInput,self.delay)

        pyautogui.typewrite(value)
        time.sleep(1)
        rgb = PIL.ImageGrab.grab().load()[self.moneyInput.x,self.moneyInput.y]
        if rgb == self.moneyInput.rgb:
            self.interrupt(" Can not input money!")
        else:
            print("\tInput",typeBtn.message, ":\tsuccessfully!")    
        # move to OK - okBtn
        self.click_n_delay(self.okBtn,1)
        if typeBtn.message == "Big":
            self.checkRGB(self.lastCheck.x,self.lastCheck.y,(255,255,255), "Before submit!!!")
            print("\t--> Submit Big")
        elif typeBtn.message == "Small":
            self.checkRGB(self.lastCheck.x,self.lastCheck.y,self.lastCheck.rgb, "Before submit!!!")
            print("\t--> Submit Small")
        
        time.sleep(2)
        # move to CONFIRM - confirmBtn
        self.click_n_delay(self.confirmBtn,3)
        self.status = 1
        # move to close information - informBtn
        rgb = PIL.ImageGrab.grab().load()[self.informBtn.x,self.informBtn.y]
        
        endtime = time.time() + 5
        while rgb != self.informBtn.rgb:
            print("Over 3s for confirmation form appear!!!")
            current_time = time.time()
            rgb = PIL.ImageGrab.grab().load()[self.informBtn.x,self.informBtn.y]
            if current_time > endtime:
                self.interrupt("CEP")
            time.sleep(1)

        self.checkRGB(self.confirmBtn.x,self.confirmBtn.y,(153,153,153), "Check after clicking submit !!!")

        self.click_n_delay(self.informBtn,self.delay)

        # TODO: Check submit button still exist or not ? 
        self.checkRGB(self.confirmBtn.x,self.confirmBtn.y,(255,255,255), "Submit failed !!!")

    def start(self):
        # m = random.randint(0,7)
        # if m == 2 or m == 3 or m == 4 or m ==7:
        #     print("\tRefresh page !")
        #     self.refreshPage()

        rgb = PIL.ImageGrab.grab().load()[self.selfCheckBtn.x,self.selfCheckBtn.y]
        if rgb == self.selfCheckBtn.rgb:
            self.interrupt("Self check RGB wrong!")
        self.checkRGB(self.crownBtn.x, self.crownBtn.y,self.crownBtn.rgb,"First check crown")
        # Check big and small before run
        self.checkRGB(self.bigBtn.x,self.bigBtn.y,self.bigBtn.rgb,"First check big")
        self.checkRGB(self.smallBtn.x,self.smallBtn.y,self.smallBtn.rgb,"First check small")
        
        # refresh NUMBER
        self.click_n_delay(self.refresNumberBtn,2)
        # n = random.randint(0,5)
        if self.status == 0:
            # CALL SMALL - BIG
            self.click_procedure(self.smallBtn, self.smallVal)
            # time.sleep(waitingClickTime[n])
            self.click_procedure(self.bigBtn, self.bigVal)
            self.status = 0

        # n = random.randint(0,1)
        # if n == 0 and self.status == 0:
        #     # CALL BIG - SMALL
        #     self.click_procedure(self.smallBtn, self.smallVal)
        #     self.click_procedure(self.bigBtn, self.bigVal)
        #     self.status = 0
        # elif n == 1 and self.status == 0:
        #     # CALL SMALL - BIG
        #     self.click_procedure(self.smallBtn, self.smallVal)
        #     self.click_procedure(self.bigBtn, self.bigVal)
        #     self.status = 0

mouse = Controller()

