import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail():
    url = 'smtp.mail.ru'

    login = input('mail отправителя: ')
    password = input('password отправителя: ')
    toaddr = input('mail кому отправлять: ')
    topic = input('Tema: ')
    message = input('message: ')

    msg = MIMEMultipart()

    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())


def main():
    send_mail()


if __name__ == '__main__':
    main()
