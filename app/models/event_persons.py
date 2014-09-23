from ferris import BasicModel, ndb
from app.models.university import University

class EventPerson(BasicModel):
	event_person_id = ndb.IntegerProperty(required=True)
	market_place_person_id = ndb.IntegerProperty()
	first_name = ndb.StringProperty()
	last_name = ndb.StringProperty()
	picture_url = ndb.StringProperty()
	emails =  ndb.StringProperty(repeated=True)


class Anchor(EventPerson):
	facebook_account = ndb.StringProperty()
	twitter_account =  ndb.StringProperty()
	biography = ndb.TextProperty()
	career =  ndb.StringProperty()


class SpeakerQuestion(BasicModel):
	question_id = ndb.StringProperty(required=True)
	sender_name = ndb.StringProperty()
	sender_email = ndb.StringProperty()
	sender_question = ndb.StringProperty()
	sender_university = ndb.LocalStructuredProperty( University )
	has_been_revised = ndb.BooleanProperty(default=False)


class Speaker(EventPerson):
	facebook_account = ndb.StringProperty()
	linkedin_account = ndb.StringProperty()
	twitter_account =  ndb.StringProperty()
	biography = ndb.TextProperty()
	biography_url = ndb.StringProperty()
	company =  ndb.StringProperty()
	#----------------------------------------
	speaker_questions = ndb.LocalStructuredProperty( SpeakerQuestion )



