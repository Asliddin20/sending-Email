import smtplib
from email.message import EmailMessage

while True:
    to_email = input('Покажити э-почту своего друга: ')
    if(to_email.find('@') == -1):
        print("Пожалуста, покажите правильную почту")
        continue
    from_name = input('От кого: ')
    title = input('Причина вашего обращение: ')
    content = input('Напишите писмо: ')
    break

email = EmailMessage()
email['from'] = from_name
email['to'] = to_email
email['subject'] = title

email.set_content(content)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email@gmail.com', 'password')
    smtp.send_message(email)
    print('all done!')
print('----------------- Если вы указали почту правельно, писмо отправлено--------------------------')
