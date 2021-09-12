import pygetwindow as gw

print(gw.getAllTitles())
print(gw.getWindowsWithTitle('MEmu'))

# 1 SCREEN
TOPLEFT_X_1 = 15
TOPLEFT_Y_1 = 10
MEMU_W_1 = 686
MEMU_H_1 = 395



# 2 SCREEN
# TOPLEFT_X = 2086
# TOPLEFT_Y = 25
# MEMU_W = 1650
# MEMU_H = 941

memudWindow  = gw.getWindowsWithTitle('MEmu')[0]
# memudWindow.activate()
# print(memudWindow.width)
# print(memudWindow.height)
# print(memudWindow.topleft)

memudWindow.moveTo(TOPLEFT_X_1, TOPLEFT_Y_1)
memudWindow.resizeTo(MEMU_W_1, MEMU_H_1)


