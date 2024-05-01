import requests
from datetime import datetime  # noted
import smtplib
import time

myemail = "the email"
password = "password"

parameter = {
    "lat" : 22.572645,
    "lng" : 88.363892,
}
response = requests.get("https://api.sunrisesunset.io/json", params = parameter)#API call using parameters allowed
response.raise_for_status()#error check
data = response.json()#data extract krne ke liye
sunrise = int(data['results']['sunrise'].split(":")[0])
sunset = int(data['results']['sunset'].split(":")[0]) + 12 #sunset to shaam ko hoga isliye +12

print(f"Sunrise timing : {sunrise}")
print(f"Sunset timing : {sunset}")

time_now = datetime.now()

#lets get the ISS position
ISS = requests.get(url = 'http://api.open-notify.org/iss-now.json')
pos = ISS.json()
latitude = float(pos['iss_position']['latitude'])
longitude = float(pos['iss_position']['longitude'])

while True:
    time.sleep(60)
    if (parameter["lat"] - 5 <= latitude <= parameter["lat"] + 5
            and parameter["lng"] - 5 <= longitude <= parameter["lng"] + 5
            and time_now < sunrise and time_now > sunset):
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=myemail, password=password)
        print("sending mail")
        connection.sendmail(from_addr=myemail,
                            to_addrs='pawanrnc.ps@gmail.com',
                            msg='Subject: ISS Overhead alert\n\n LOOK UP!')
        connection.close()
