#darkskyapi

import requests, json, smtplib

#(key, lat, long)
parameters = ('4454cd0f9b09f3329eea2f6b77a8752e', '37.8267', '-122.4233')

apiResponse = requests.get('https://api.darksky.net/forecast/%s/%s,%s?exclude=[minutely,hourly,alerts,flags]' % parameters)

#should print 200
#print(apiResponse.status_code)

#data is a python dict
data = apiResponse.json()

#prints .json object in the form of a dict
#print(data)

#summary of weather report
summary = 'The temperature is %s with a high of %s and a low of %s' % (data['currently']['temperature'], data['daily']['data'][0]['temperatureHigh'], data['daily']['data'][0]['temperatureLow'])



gmail_user = HIDDEN
gmail_password = HIDDEN
recipient = HIDDEN

message = '''From: %s\nTo: %s\nSubject: %s\n\n%s
    ''' % (gmail_user, recipient, 'Weather Update', summary)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, recipient, message)
    server.close()
    print('Sent to %s' % recipient)
except:  
    print('Error')