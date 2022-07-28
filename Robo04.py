import pyautogui as p

p.doubleClick(x=36, y=226)
p.sleep(4)
p.write('www.udemy.com')
p.press('enter')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(3)

localPesq = p.locateOnScreen('Pesquisa.PNG', confidence=0.8)
localPesquisa = p.center(localPesq)
xPesquisa, yPesquisa = localPesquisa
p.moveTo(xPesquisa, yPesquisa, duration=1)
p.click(xPesquisa, yPesquisa)
p.sleep(1)
p.write('Charles Lima')
p.press('enter')
p.sleep(3)
p.screenshot('Cursos.png')
p.sleep(3)

localClo = p.locateOnScreen('Close.PNG', confidence=0.9)
localClose = p.center(localClo)
xClose, yClose = localClose
p.moveTo(xClose, yClose, duration=1)
p.click(xClose, yClose)


# p.sleep(2)
# print(p.position())