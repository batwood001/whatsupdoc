import time, requests
from src.notifications import slack, email, sms
from src.config import config

def start():
	c = config.get()
	print('Waiting', c.startup_delay, 'seconds ...')
	time.sleep(c.startup_delay) 
	print('Starting heartbeat ...')
	consecutive_failures = 0

	while consecutive_failures < c.failures:
		print('Checking ...')
		try:
			response = requests.get(url=c.endpoint, timeout=c.timeout)

			if response.status_code == 200:
				consecutive_failures = 0
				print('Success')
			else:
				consecutive_failures += 1
				print('Fail')

		except Exception as e:
			consecutive_failures += 1
			print('Fail')

		if consecutive_failures < c.failures:
			time.sleep(c.interval)


	notifs_sent = 0
	# send at most 50 notifications
	while notifs_sent < min(c.max_notifications, 50):
		# send a notification at most every 5 minutes
		send_notifications()
		notifs_sent += 1
		time.sleep(max(c.notification_interval, 300))
		


def send_notifications():
	c = config.get()
	for destination in [slack, email, sms]:
		module_name = destination.__name__.split('.')[-1]
		if c.notifications[module_name]['enabled']:
			dest_config = c.notifications[module_name]
			kwargs = {k: dest_config[k] for k in dest_config if k != 'enabled'}
			destination.send(**kwargs)
