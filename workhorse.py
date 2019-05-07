import yaml

class automationHours():
	def __init__(self, action):
		with open("config.yml", 'r') as ymlFile:
			cfg = yaml.load(ymlFile, Loader=yaml.FullLoader)

		if action == 'listing':
			self.ymlaction = cfg['listingproject']

		elif action == 'manifest':
			print('pazz')
			pass

		elif action == 'taxes':
			self.ymlaction = cfg['taxesproject']

		for each in range(3):
			self.ymlaction['totaltimesaved'] += self.ymlaction['timesavedperrun']
			self.ymlaction['totalruncounter'] += 1
			self.ymlaction['message'] = 'Times Ran: %s\nTime Saved: %s %s\n' % (self.ymlaction['totalruncounter'], self.ymlaction['totaltimesaved'], self.ymlaction['timesavedunit'])
			print(self.ymlaction['message'])

		with open("config.yml", "w") as f:
	   		yaml.dump(cfg, f)

	def createImg(self):
		message = self.ymlaction['message']
		print message

x = automationHours('taxes').createImg()
