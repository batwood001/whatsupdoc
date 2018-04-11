import json, argparse, sys

parser = argparse.ArgumentParser(description='Start a healthcheck service')
parser.add_argument('config_path', metavar='json_config_path', type=str,
                   help='absolute or relative path to the json config')

args = parser.parse_args()

config = None
try:
	config = json.load(open(args.config_path))
except Exception as e:
	print('Failed to open', args.config_path, ':', e)
	sys.exit()

print(config)


# required: 
# - path/to/config


# print('hello world')

# def main():


# if __name__ == '__main__':
# 	main()

