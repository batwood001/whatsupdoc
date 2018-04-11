import time, requests

from src.notifications import slack, email, sms

def start(config):
	print('Waiting', config.startup_delay, 'seconds ...')
	time.sleep(config.startup_delay) 
	print('Starting heartbeat ...')
	consecutive_failures = 0

	while consecutive_failures < config.failures:
		print('Checking ...')
		try:
			response = requests.get(url=config.endpoint, timeout=config.timeout)

			if response.status_code == 200:
				consecutive_failures = 0
				print('Success')
			else:
				consecutive_failures += 1
				print('Fail')

		except Exception as e:
			consecutive_failures += 1
			print('Fail')

		if consecutive_failures < config.failures:
			time.sleep(config.interval)

	send_notifications(config)


def send_notifications(config):
	for destination in [slack, email, sms]:
		module_name = destination.__name__.split('.')[-1]
		if config.notifications[module_name]['enabled']:
			dest_config = config.notifications[module_name]
			kwargs = {k: dest_config[k] for k in dest_config if k != 'enabled'}
			destination.send(**kwargs)
