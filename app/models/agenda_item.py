from ferris import BasicModel, ndb
from app.models.speaker import Speaker

class AgendaItem(BasicModel):
	title = ndb.StringProperty(required=True)
	start_datetime = ndb.DateTimeProperty()
	end_datetime = ndb.DateTimeProperty()
	active = ndb.BooleanProperty()
	speakers = ndb.LocalStructuredProperty( Speaker , repeated=True )