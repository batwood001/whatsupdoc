import json, argparse, sys, functools
from types import SimpleNamespace
from src import heartbeat
from src.config import config

parser = argparse.ArgumentParser(description='Start a healthcheck service')
parser.add_argument(
	'config_path',
	metavar='json_config_path',
	type=str,
	help='absolute or relative path to the json config'
)

args = parser.parse_args()

try:
	config_json = json.load(open(args.config_path))
	config.set(SimpleNamespace(**config_json))
except Exception as e:
	print('Failed to open', args.config_path, ':', e)
	sys.exit()

heartbeat.start()