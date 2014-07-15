import json

class TwitterAsync(object):
	def __init__(self, a_fileName):
		self.fileName = a_fileName

	def fileData():
		doc = "The fileData property."
		def fget(self):
			with open(self.fileName, mode='w+') as f:
				try:
					self._fileData = json.load(f)
				except ValueError, e:
					print 'no es un json valido, devolviendo array vacio'
					self._fileData = []
			return self._fileData
		def fset(self, value):
			with open(self.fileName, mode='w') as f:
				try:
					json.dump(value, f)
				except ValueError, e:
					print "awdawdawdawdawdawd"
			self._fileData = value
		def fdel(self):
			del self._fileData
		return locals()
	fileData = property(**fileData())

	def Enqueue(self, message, media=''):
		data = {}
		data['message'] = message

		if media != '':
			data['media'] = media

		self.fileData.append(data)

		print json.dumps(self.fileData)
		#self.WriteDataToFile()

t = TwitterAsync("file.json")
t.Enqueue("hola")