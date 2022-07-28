import pyautogui as p

p.hotkey('win','r')
p.sleep(1)
p.write('C:\RPA.pbix')
p.sleep(1)
p.press('enter')
p.sleep(30)
p.click(x=566, y=90)
p.sleep(10)
p.click(x=1339, y=14)
p.sleep(5)
p.click(691, 404)

# p.sleep(3)
# print(p.position())
