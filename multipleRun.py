import time
# from pynput.keyboard import Listener, KeyCode
# from pynput import keyboard
# from pynput.mouse import Button, Controller
# from datetime import datetime
import pyautogui
import random
import winsound
# import PIL.ImageGrab
from buttonClass import *


delay = 0.5
button =  Button.left
start_stop_key = keyboard.KeyCode(char='z')
exit_key = keyboard.Key.esc


INITIAL_PLAY_NUMBER = 92
# acc1
cap = 334000
refreshPageBtn = btn(800,104,"Refresh Page" ,(0,0,0))
crownBtn = btn(60,357,"Crown btn",(241,49,49))
refresNumberBtn = btn(710,213,"F5 Number",(239, 141, 134))
bigBtn = btn(462,380,"Big", (255,255,255)) #btn(416,875,())
smallBtn = btn(813,382,"Small",(255,255,255)) #btn(626,875)
moneyInput = btn(501,451,"Money Input",(175,175,175))
okBtn = btn(710,452,"Ok",(241, 49, 49))
submitBtn = btn(361,429,"Submit",(255, 0, 0))
selfCheckBtn = btn(562,370,"Self Check",(65, 35, 242))
informBtn = btn(406,355,"Confirm",(4, 124, 255))
menuBtn = btn(803,152,"Menu",(242,64,64))
recordBtn = btn(745,303,"Record btn",(252,252,252))
removeBtn = btn(583,254,"Remove btn",(78,162,255))
confirmRm = btn(473,376,"Confirm Remove btn",(250,250,250))
lastcheckBtn = btn(385,356,"Confirm Remove btn",(80,80,80)) 
runIns = run(refreshPageBtn, crownBtn, refresNumberBtn, bigBtn, smallBtn, moneyInput, okBtn, submitBtn, selfCheckBtn, 
                    informBtn,menuBtn,recordBtn,removeBtn,confirmRm,cap, lastcheckBtn,0)
runIns.profitBound = 1000

# acc2
cap1 = 75800
refreshPageBtn1 = btn(800,610,"Refresh Page" ,(0,0,0))
crownBtn1 = btn(60,863,"Crown btn",(241,49,49))
refresNumberBtn1 = btn(710,719,"F5 Number",(239, 141, 134))
bigBtn1 = btn(462,886,"Big", (255,255,255)) #btn(416,875,())
smallBtn1 = btn(813,888,"Small",(255,255,255)) #btn(626,875)
moneyInput1 = btn(501,957,"Money Input",(175,175,175))
okBtn1 = btn(710,958,"Ok",(241, 49, 49))
submitBtn1 = btn(361,935,"Submit",(255, 0, 0))
selfCheckBtn1 = btn(562,876,"Self Check",(65, 35, 242))
informBtn1 = btn(406,861,"Confirm",(4,124,255))
menuBtn1 = btn(803,658,"Menu",(242,64,64))
recordBtn1 = btn(745,809,"Record btn",(252,252,252))
removeBtn = btn(558,760,"Remove btn",(20,132,255))
confirmRm1 = btn(473,882,"Confirm Remove btn",(250,250,250))
lastcheckBtn1 = btn(385,862,"Confirm Remove btn",(80,80,80)) 

runIns1 = run(refreshPageBtn1, crownBtn1, refresNumberBtn1, bigBtn1, smallBtn1, moneyInput1, okBtn1, submitBtn1, selfCheckBtn1, 
                    informBtn1,menuBtn1,recordBtn1,removeBtn,confirmRm1,cap1,lastcheckBtn1,506)

# runAll = [runIns, runIns1]

separateRun = [3,5,11,7,2,0]

class Program():
    def __init__(self):
        super().__init__()
        self.running = False
        self.program_running = True
        self.count = 1
        self.minusFlag = False
        self.plusFlag = False
        
    def start_auto(self):
        self.running = True
        print("Start now\n")
        self.run()

    # def stop_auto(self):
    #     self.running = False
    #     print("Stop now")

    # def exit(self):
    #     self.stop_auto()
    #     self.program_running  = False
    
    def run(self):
        frequency = 2500  # Set Frequency To 2500 Hertz
        # duration = 1000  # Set Duration To 1000 ms == 1 second
        while self.program_running:
            while self.running:
                start_time = time.perf_counter()
                print(time.strftime('%X %x %Z'))
                
                winsound.Beep(frequency, 600)
                winsound.Beep(frequency, 600)
                winsound.Beep(frequency, 600)
                
                print("Time  ------- {} -------- {}".format(self.count, self.count -1 + INITIAL_PLAY_NUMBER))
                # time.sleep(1)
                print("...3")
                time.sleep(1)
                print("...2")
                time.sleep(1)
                print("...1")
                time.sleep(1)
                print("...0")
                
                
                n = random.randint(0,5)
                # time.sleep(separateRun[n])
                if n % 2 == 0:
                    # RUN ACC 0
                    print("---> Run acc 0: Cap:{} \tBig:{} \tSmall:{} ".format(runIns.cap, runIns.bigVal, runIns.smallVal))
                    print("\tProfit: ", runIns.profit)
                    runIns.start()
                    runIns.calProfitNewCap()
                    # RUN ACC 1
                    print("---> Run acc 1: Cap:{} \tBig:{} \tSmall:{} ".format(runIns1.cap, runIns1.bigVal, runIns1.smallVal))
                    print("\tProfit: ", runIns1.profit)
                    runIns1.start()
                    runIns1.calProfitNewCap()
                else:
                    # RUN ACC 1
                    print("---> Run acc 1: Cap:{} \tBig:{} \tSmall:{} ".format(runIns1.cap, runIns1.bigVal, runIns1.smallVal))
                    print("\tProfit: ", runIns1.profit)
                    runIns1.start()
                    runIns1.calProfitNewCap()
                    # RUN ACC 0
                    print("---> Run acc 0: Cap:{} \tBig:{} \tSmall:{} ".format(runIns.cap, runIns.bigVal, runIns.smallVal))
                    print("\tProfit: ", runIns.profit)
                    runIns.start()
                    runIns.calProfitNewCap()
                     
                # # TODO: for future, having more than 2 ins
                # # for r in runAll:
                # #     print("\tRun acc {0}: Cap:{1} \tBig:{2} \tSmall:{3} ".format(runAll.index(r), r.cap, r.bigVal, r.smallVal))
                # #     r.start()
                # #     # reset mouse position to prevent unknown action
                # #     pyautogui.moveTo(920, 520, duration = 1)
                # #     time.sleep(separateRun[n])
                # # move mouse out of activate window to prevent unknown action
               
                print("Check Order acc 1:")
                runIns1.checkOrder()
                print("Check Order acc 0:")
                runIns.checkOrder()

                runIns.refreshPage()
                runIns1.refreshPage()

                pyautogui.moveTo(920, 520, duration = 1)
                print("End   ------- {} -------- {} -------------------------------".format(self.count, self.count -1 + INITIAL_PLAY_NUMBER))
                self.count = self.count + 1
                winsound.Beep(frequency, 300)

                if self.count == 25:
                    self.running = False
                    print("Please reset me!")
                    exit()
                
                elapsed_t = time.perf_counter() - start_time
                print("Run time: ", elapsed_t)
                n = random.randint(1,4)
                if n%3 == 1 and self.plusFlag == False:
                    self.plusFlag = True
                    self.minusFlag = False
                    time.sleep(310 - elapsed_t)
                elif n%3 == 2 and self.minusFlag == False:
                    self.minusFlag = True
                    self.plusFlag = False
                    time.sleep(290 - elapsed_t)
                else:
                    time.sleep(300 - elapsed_t)

runProg =  Program()
runProg.start_auto()
                
