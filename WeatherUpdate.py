#WeatherUpdate using AWS

import requests, json, boto3

#(API key, lat, long)
parameters = ('4454cd0f9b09f3329eea2f6b77a8752e', '31.2304', '-121.4737')

apiResponse = requests.get('https://api.darksky.net/forecast/%s/%s,%s?exclude=[minutely,hourly,alerts,flags]' % parameters)

#data is a python dict
data = apiResponse.json()

#summary of weather report
summary = 'The temperature is %s with a high of %s and a low of %s' % (data['currently']['temperature'], data['daily']['data'][0]['temperatureHigh'], data['daily']['data'][0]['temperatureLow'])


client = boto3.client('sns','us-east-1')

phoneNumber = #phonenumber
message = summary


client.publish(PhoneNumber=phoneNumber, Message=message)
#git test
