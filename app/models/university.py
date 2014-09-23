from ferris import BasicModel, ndb

class University(BasicModel):
	acronym = ndb.StringProperty(required=True)
	name = ndb.StringProperty()
	description = ndb.TextProperty()