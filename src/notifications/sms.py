from twilio.rest import Client
from src.config import config

def send(numbers, message):
  twilio = config.get().auth['twilio']
  client = Client(
    twilio['account_sid'],
    twilio['auth_token']
  )

  print('Sending SMS notifications ...')
  for number in numbers:
    message = client.messages.create(
      to="+1" + str(number), 
      from_=twilio['from'],
      body=message)

    print(message.sid)

