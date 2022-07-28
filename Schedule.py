import schedule
import time
from Robo01 import BotRobo01
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    print('Iniciou..')

    schedule.every().day.at("18:29").do(BotRobo01)
    schedule.every().day.at("19:29").do(BotRobo01)

    while True:
        schedule.run_pending()
        time.sleep(1)

except IndexError as e:
    # texto do email
    texto_email =  f'''
                    O bot notepade falhou, por gentileza, verificar.
                    Erro: {e}
                    '''

    # email remetente, senha, destinatário
    de = 'cursorpapython@gmail.com'
    senha = '**********'
    para = 'cursorpapython@gmail.com'
    #para02 = 'cursorpapython@gmail.com'

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = de
    message['To'] = para
    #message['To'] = para02
    message['Subject'] = 'BotNotepad Falhou!!'  # Título do e-mail

    # Corpo do E-mail com anexos
    message.attach(MIMEText(texto_email, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
    session.starttls()  # Habilita a segurança
    session.login(de, senha)  # Login e senha de quem envia o e-mail
    texto = message.as_string()
    session.sendmail(de, para , texto)
    session.quit()