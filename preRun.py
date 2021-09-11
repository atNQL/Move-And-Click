import pygetwindow as gw

print(gw.getAllTitles())
print(gw.getWindowsWithTitle('MEmu'))

# 1 SCREEN
TOPLEFT_X = 20
TOPLEFT_Y = 65
MEMU_W = 844
MEMU_H = 485

# 2 SCREEN
# TOPLEFT_X = 2086
# TOPLEFT_Y = 25
# MEMU_W = 1650
# MEMU_H = 941

memudWindow  = gw.getWindowsWithTitle('MEmu')[0]
# print(memudWindow.width)
# print(memudWindow.height)
memudWindow.moveTo(TOPLEFT_X, TOPLEFT_Y)
# memudWindow.resizeTo(MEMU_W, MEMU_H) # 2 SCREEN


