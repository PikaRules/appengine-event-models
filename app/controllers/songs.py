from ferris import Controller, route
from app.models.artist import Artist
from app.models.song import Song
from app.tools.request_helper import RequestHelper
import json
import sys


class Songs(Controller,RequestHelper):
	class Meta:
		View = 'json'
		prefixes = ('api',)


	@route
	def api_getAll(self):
		self.setCordsHeaders()
		songs = Song.all()
		self.context['data'] = songs	

	@route
	def api_addNew( self ):
		self.setCordsHeaders()
		try:
			jsonObject = self.getPostDataObject()
			title = jsonObject.get('title','')
			"""description = jsonObject.get('description','')
			self.context['data'] = jsonObject
			if name :
				newFoo = Song( name = name, description = description )
				newFoo.put()"""
		except:
			self.context['data'] = sys.exc_info()