import requests

def send(webhooks, message):
	print('Sending slack notifications ...')
	for hook in webhooks:
		data = {
			'text': message
		}
		res = requests.post(url=hook, json=data)
