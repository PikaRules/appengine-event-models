from ferris import ndb

class StringTranslationProperty(ndb.StringProperty):
	def _validate()