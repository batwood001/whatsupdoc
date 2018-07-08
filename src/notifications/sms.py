from twilio.rest import Client
import config

# Your Account SID from twilio.com/console
account_sid = "AC0f9ba402683abc0200c5be046b3584c1"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(
  config.auth.twilio.account_sid,
  config.auth.twilio.auth_token
)


def send(numbers, message):
  print('Sending SMS notifications ...')
  for number in numbers:
    message = client.messages.create(
      to="+1" + str(number), 
      from_="+1" + str(number),
      body=message)


  print(message.sid)