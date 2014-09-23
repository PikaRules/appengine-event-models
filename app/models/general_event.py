from ferris import BasicModel, ndb
from app.models.agenda_item import AgendaItem
from app.models.anchor import Anchor
from app.models.participant import Participant
from app.models.properties.translations import *

class GeneralEvent(BasicModel):
	event_id = ndb.IntegerProperty(required=True)
	name_id = ndb.IntegerProperty(required=True)
	name = ndb.StringProperty(required=True)
	privacy = ndb.StringProperty( choices=( 'Private','Public','Secret' ) )
	picture =  ndb.StringProperty()
	start_datetime = ndb.DateTimeProperty()
	end_datetime = ndb.DateTimeProperty()
	languages = ndb.StringProperty( choices=( 'English','Spanish','Portugese' ) )
	location = ndb.StringProperty()
	active = ndb.BooleanProperty()

	#agenda_items = ndb.StructuredProperty( AgendaItem , repeated=True )
	#participants = ndb.StructuredProperty( Participant , repeated=True )
	#anchors = ndb.StructuredProperty( Anchor , repeated=True )

	description = StringTranslationProperty()
	title = ChoiceTranslationProperty( spanish_choices=( 'hola','pepino' ),english_choices=( 'hello','cucumber'),portuguese_choices=( 'ajo','toto' ) )