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

delay = 1
button =  Button.left

start_stop_key = keyboard.KeyCode(char='z')
# {keyboard.Key.cmd, keyboard.Key.ctrl}
exit_key = keyboard.Key.esc
# key == keyboard.Key.esc

# BIG_VAL   = CAP*0.4709
# SMALL_VAL = CAP*0.5291
# 2125, 1891

# 1 screen

INITIAL_PLAY_NUMER = 113
cap = 34600
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
removeBtn = btn(558,254,"Remove btn",(20,132,255))
confirmRm = btn(473,376,"Confirm Remove btn",(250,250,250))

runIns1 = run(refreshPageBtn, crownBtn, refresNumberBtn, bigBtn, smallBtn, moneyInput, okBtn, submitBtn, selfCheckBtn, 
                    informBtn,menuBtn,recordBtn,removeBtn,confirmRm,cap)
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

class Program():
    def __init__(self):
        super().__init__()
        self.running = False
        self.program_running = True
        self.count = 1
        self.minusFlag = False
        self.plusFlag = False
        self.profit = 0
        

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
                print(time.strftime('%X %x %Z'))
                
                print("Profit: ", runIns1.profit)
                winsound.Beep(frequency, 600)
                winsound.Beep(frequency, 600)
                winsound.Beep(frequency, 600)
                start_time = time.perf_counter()
                print("Time  ------- {} -------- {}".format(self.count, self.count -1 + INITIAL_PLAY_NUMER))
                time.sleep(1)
                print("...3")
                time.sleep(1)
                print("...2")
                time.sleep(1)
                print("...1")
                time.sleep(1)
                print("...0")
                
                print("\tRun : Cap:{0} \tBig:{1} \tSmall:{2} ".format(runIns1.cap, runIns1.bigVal, runIns1.smallVal))
                runIns1.start()
                # move mouse out of activate window to prevent unknown action
                pyautogui.moveTo(920, 520, duration = 1)
                runIns1.calProfitNewCap()
                print("End   ------- {} -------- {} -------------------------------".format(self.count, self.count -1 + INITIAL_PLAY_NUMER))
                self.count = self.count + 1
                winsound.Beep(frequency, 300)

                if self.count == 25:
                    self.running = False
                    print("Please reset me!")
                    exit()
                
                elapsed_t = time.perf_counter() - start_time
                n = random.randint(1,4)
                if n%3 == 0:
                    time.sleep(300 - elapsed_t)
                elif n%3 == 1:
                    if self.plusFlag == False:
                        self.plusFlag = True
                        self.minusFlag = False
                        time.sleep(320 - elapsed_t)
                    else:
                        time.sleep(300 - elapsed_t)
                elif n%3 == 2:
                    if self.minusFlag == False:
                        self.minusFlag = True
                        self.plusFlag = False
                        time.sleep(280 - elapsed_t)
                    else:
                        time.sleep(300 - elapsed_t)

runProg =  Program()
runProg.start_auto()
