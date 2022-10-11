def sent_mail():
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=gmail, password=password)
    connection.sendmail(from_addr=gmail, to_addrs='samplemail1511@yahoo.com', msg=f'subject:ISS APPROACH\n\n'
                                                                  f'You are lucky!, ISS is approaching you in the '
                                                                  f'night sky, '
                                                                  f'Go out and look up to see ISS crossing you in the '
                                                                  f'sky...')
    print("mail sent")
    connection.close()


def is_dark():
    parameters = {'lat': my_latitude,
                  'lng': my_longitude,
                  'formatted': 0
                  }
    sunrise_data = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    sunrise_time = int(sunrise_data.json()['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_time = int(sunrise_data.json()['results']['sunset'].split('T')[1].split(':')[0])

    current_time = datetime.datetime.now().hour
    if current_time >= sunset_time or current_time <= sunrise_time:
        return True

def position_check():
    iss_data = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_latitude = float(iss_data.json()['iss_position']['latitude'])
    iss_longitude = float(iss_data.json()['iss_position']['longitude'])

    if (my_latitude - 5 < iss_latitude < my_latitude + 5) and (my_longitude - 5 < iss_longitude < my_longitude + 5):
        return True


import requests
import datetime
import smtplib

gmail = 'samplemail1511@gmail.com'
password = 'pnxonvoqufyhxdyj'
my_latitude = 43.653225
my_longitude = -79.383186

if position_check():
    if is_dark():
        sent_mail()
