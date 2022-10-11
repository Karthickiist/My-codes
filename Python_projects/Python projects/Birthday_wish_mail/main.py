import smtplib
import datetime
import random
import pandas

def send_mail():
    connection=smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls()
    connection.login(user=gmail, password=password)
    connection.sendmail(from_addr=gmail, to_addrs=i['email'],msg=f'subject:Happy birthday\n\n'
                                                                 f'{wish}')
    print("mail sent")
    connection.close()
gmail='samplemail1511@gmail.com'
password='pnxonvoqufyhxdyj'

data=pandas.read_csv('birthdays.csv')
data_dict=data.to_dict('records')
time=datetime.datetime.now()
month=time.month
day=time.day
letters=[]
with open('./letter_templates/letter_1.txt','r') as f:
    letters.append(f.read())
with open('./letter_templates/letter_2.txt','r') as f:
    letters.append(f.read())
with open('./letter_templates/letter_3.txt','r') as f:
    letters.append(f.read())
for i in data_dict:
    if i['month']==month and i['day']==day:
        wish=random.choice(letters).replace('[NAME]',i['name'])
        send_mail()



