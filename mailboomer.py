import smtplib
from getpass import getpass

print ("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print ("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|              By rmznbyv                  \033[1;m")
print ("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|        Copyright (c) 2022 rmznbyv          \033[1;m")
print ("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __   __         __  ___     \033[1;m")
print ("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |  | |\/|  |__  |__|    \033[1;m")
print ("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |__| |  |  |__  |  \    \033[1;m")
print(" ")
pri
your_mail = input("Input your YandexMail addres: ")
your_pass = getpass("Input your YandexMail password: ")
target_mail = input("Input target mail: ")
title = input("Input message title: ")
msg = input("Input message: ")

def send_emails(title,msg):
    server = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
    server.ehlo()
    server.starttls()
    server.login(your_mail, your_pass)
    message = 'Subject: {}\n\n{}'.format(title,msg)
    server.sendmail(your_mail, target_mail, message)
    server.quit()
    print('E-mails successfully sent!')