from buttonClass import *
import pyautogui, sys
import PIL.ImageGrab
import time

cap = 370000
refreshPageBtn = btn(800,104,"Refresh Page" ,(0,0,0))
crownBtn = btn(60,357,"Crown btn",(241,49,49))
refresNumberBtn = btn(710,213,"F5 Number",(239, 141, 134))
bigBtn = btn(462,382,"Big", (255,255,255)) #btn(416,875,())
smallBtn = btn(813,382,"Small",(255,255,255)) #btn(626,875)
moneyInput = btn(501,451,"Money Input",(175,175,175))
okBtn = btn(710,452,"Ok",(241, 49, 49))
submitBtn = btn(361,429,"Submit",(255, 0, 0))
selfCheckBtn = btn(562,370,"Self Check",(65, 35, 242))
informBtn = btn(406,355,"Confirm",(4, 124, 255))
menuBtn = btn(803,152,"Menu",(242,64,64))
recordBtn = btn(745,303,"Record btn",(252,252,252))
removeBtn = btn(583,254,"Remove btn",(78,162,255))
removeBtn1 = btn(583,338,"Confirm Remove btn",(78,162,255))
confirmRm = btn(473,376,"Confirm Remove btn",(250,250,250))
# removeBtn1 = btn(583,339,"Confirm Remove btn",(250,250,250))
lastcheckbtn = btn(385,862,"Confirm Remove btn",(250,250,250)) #(80,80,80)

tupleBtn =[refreshPageBtn, crownBtn, refresNumberBtn, bigBtn, smallBtn, moneyInput, okBtn, submitBtn, selfCheckBtn, 
                    informBtn,menuBtn,recordBtn,removeBtn,confirmRm]
tupleBtn1 =[bigBtn, smallBtn]

nhoCheck = btn(459,381,"Confirm Remove btn",(150, 150, 150))
lonCheck = btn(459,381,"Confirm Remove btn",(174, 174, 174))
iconCheck = btn(221,209,"Icon Check",(91,154,223))
backBtn = btn(201,151,"Back record btn", (241,49,49))

nhoCheck1 = btn(459,887,"Confirm Remove btn",(150, 150, 150))
lonCheck1 = btn(459,887,"Confirm Remove btn",(174, 174, 174))
backBtn1 = btn(201,657,"Back record btn", (241,49,49))
iconCheck1 = btn(221,715,"Icon Check",(91,154,223))

offSetPos = 506


# refreshPageBtn1 = btn(800,610,"Refresh Page" ,(0,0,0))
# crownBtn1 = btn(60,863,"Crown btn",(241,49,49))
# refresNumberBtn1 = btn(710,719,"F5 Number",(239, 141, 134))
# bigBtn1 = btn(462,886,"Big", (255,255,255)) #btn(416,875,())
# smallBtn1 = btn(813,888,"Small",(255,255,255)) #btn(626,875)
# moneyInput1 = btn(501,957,"Money Input",(175,175,175))
# okBtn1 = btn(710,958,"Ok",(241, 49, 49))
# submitBtn1 = btn(361,935,"Submit",(255, 0, 0))
# selfCheckBtn1 = btn(562,876,"Self Check",(65, 35, 242))
# informBtn1 = btn(406,861,"Confirm",(4,124,255))


# menuBtn = btn(803,658,"Menu",(242,64,64))
# recordBtn = btn(745,809,"Record btn",(252,252,252))
# removeBtn = btn(558,760,"Remove btn",(20,132,255))
# confirmRm = btn(473,882,"Confirm Remove btn",(250,250,250))
pyautogui.moveTo(backBtn.x,backBtn.y,1)
rgb = PIL.ImageGrab.grab().load()[backBtn.x,backBtn.y]
strOut = backBtn.message + ": " + str(rgb)
if rgb == backBtn.rgb:
    strOut = strOut + "---> Correct!\n"
else:
    strOut = strOut + "---> Incorrect!\n"
print(strOut, end='')

pyautogui.moveTo(backBtn1.x,backBtn1.y,1)
rgb = PIL.ImageGrab.grab().load()[backBtn1.x,backBtn1.y]
strOut = backBtn1.message + ": " + str(rgb)
if rgb == backBtn1.rgb:
    strOut = strOut + "---> Correct!\n"
else:
    strOut = strOut + "---> Incorrect!\n"
print(strOut, end='')


# pyautogui.moveTo(removeBtn.x,removeBtn.y,1)
# rgb = PIL.ImageGrab.grab().load()[removeBtn.x,removeBtn.y]
# strOut = removeBtn.message + ": " + str(rgb)
# if rgb == removeBtn.rgb:
#     strOut = strOut + "---> Correct!\n"
# else:
#     strOut = strOut + "---> Incorrect!\n"
# print(strOut, end='')

# time.sleep(3)

# pyautogui.moveTo(removeBtn1.x,removeBtn1.y,1)
# rgb = PIL.ImageGrab.grab().load()[removeBtn1.x,removeBtn1.y]
# strOut = removeBtn1.message + ": " + str(rgb)
# if rgb == removeBtn1.rgb:
#     strOut = strOut + "---> Correct!\n"
# else:
#     strOut = strOut + "---> Incorrect!\n"
# print(strOut, end='')

# for i in range(14):
#     pyautogui.moveTo(tupleBtn[i].x,tupleBtn[i].y,1)
#     rgb = PIL.ImageGrab.grab().load()[tupleBtn[i].x,tupleBtn[i].y]
#     strOut = tupleBtn[i].message + ": " + str(rgb)
#     if rgb == tupleBtn[i].rgb:
#         strOut = strOut + "---> Correct!\n"
#     else:
#         strOut = strOut + "---> Incorrect!\n"
#     print(strOut, end='')

