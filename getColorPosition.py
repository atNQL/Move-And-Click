from buttonClass import *
import pyautogui, sys
import PIL.ImageGrab

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
removeBtn = btn(558,254,"Remove btn",(20,132,255))
confirmRm = btn(473,376,"Confirm Remove btn",(250,250,250))

tupleBtn =[refreshPageBtn, crownBtn, refresNumberBtn, bigBtn, smallBtn, moneyInput, okBtn, submitBtn, selfCheckBtn, 
                    informBtn,menuBtn,recordBtn,removeBtn,confirmRm]
tupleBtn1 =[bigBtn, smallBtn]

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

pyautogui.moveTo(informBtn.x,informBtn.y,1)
rgb = PIL.ImageGrab.grab().load()[informBtn.x,informBtn.y]
strOut = informBtn.message + ": " + str(rgb)
if rgb == informBtn.rgb:
    strOut = strOut + "---> Correct!\n"
else:
    strOut = strOut + "---> Incorrect!\n"
print(strOut, end='')

# for i in range(14):
#     pyautogui.moveTo(tupleBtn[i].x,tupleBtn[i].y,1)
#     rgb = PIL.ImageGrab.grab().load()[tupleBtn[i].x,tupleBtn[i].y]
#     strOut = tupleBtn[i].message + ": " + str(rgb)
#     if rgb == tupleBtn[i].rgb:
#         strOut = strOut + "---> Correct!\n"
#     else:
#         strOut = strOut + "---> Incorrect!\n"
#     print(strOut, end='')

