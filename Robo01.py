import pyautogui as p
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def BotRobo01():
    p.FAILSAFE = False
    p.hotkey('win','r')
    p.sleep(1)
    p.typewrite('notepad')
    p.sleep(2)
    p.press('enter')
    p.sleep(2)
    p.typewrite('Oi!! Eu sou um Bot!')
    p.sleep(2)
    valor = p.getActiveWindow()
    valor.close()
    p.press('right')
    p.sleep(2)
    p.press('enter')
#BotRobo01()


# p.sleep(2)
# print(p.position())