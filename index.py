import json, argparse, sys, functools

from types import SimpleNamespace

from src import heartbeat

parser = argparse.ArgumentParser(description='Start a healthcheck service')
parser.add_argument(
	'config_path',
	metavar='json_config_path',
	type=str,
	help='absolute or relative path to the json config'
)

args = parser.parse_args()

config = None
try:
	config = json.load(open(args.config_path))
	config = SimpleNamespace(**config)
except Exception as e:
	print('Failed to open', args.config_path, ':', e)
	sys.exit()

heartbeat.start(config)