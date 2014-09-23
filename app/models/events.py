from ferris import BasicModel, ndb
from app.models.agenda_item import AgendaItem
from app.models.anchor import Anchor
from app.models.participant import Participant
from app.models.properties.translations import *


class GeneralEvent(BasicModel):
	event_id = ndb.IntegerProperty(required=True)
	keyname = ndb.StringProperty(required=True)
	name = ndb.StringProperty()
	privacy = ndb.StringProperty( key_value='Private', choices=( 'Private','Public','Secret' ) )
	picture =  ndb.StringProperty()
	start_datetime = ndb.DateTimeProperty()
	end_datetime = ndb.DateTimeProperty()
	languages = ndb.StringProperty( choices=( 'English','Spanish','Portugese' ) )
	location = ndb.StringProperty()
	active = ndb.BooleanProperty()

	#agenda_items = ndb.LocalStructuredProperty( AgendaItem , repeated=True )
	#participants = ndb.StructuredProperty( Participant , repeated=True )
	#anchors = ndb.StructuredProperty( Anchor , repeated=True )

	description = StringTranslationProperty()
	title = ChoiceTranslationProperty( ChoiceTranslationProperty( choices= {
		'choice1': {
			'spanish': 'mango',
			'english': 'mangon',  
		},
		'choice2': {
			'spanish': 'tomate',
			'english': 'tomato',  
		},
		'choice3': {
			'spanish': 'pollo',
			'english': 'chicken',  
		}
	}))


class VideoCastEvent(GeneralEvent):
	live_event_type = ndb.StringProperty( choices=('Speciality','Mega', 'Regional') )
	is_on_testing_mode = ndb.BooleanProperty(default=False)
	has_all_confirmed_speakers = ndb.BooleanProperty(default=False)
	agenda_url = ndb.StringProperty()
	subtitles = ndb.StringProperty( choices=('Spanish','English','Portuguese') )


class CommunityEvent(GeneralEvent):
	hola = ndb.StringProperty()


class ExternalEvent(GeneralEvent):
	is_all_day_event = ndb.BooleanProperty(default=False)
	subtitles = ndb.StringProperty( choices=('Spanish','English','Portuguese') )