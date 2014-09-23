from ferris import BasicModel, ndb

class Participant(BasicModel):
	event_person_id = ndb.IntegerProperty(required=True)
	market_place_person_id = ndb.IntegerProperty()
	first_name = ndb.StringProperty()
	last_name = ndb.StringProperty()
	picture_url = ndb.StringProperty()
	email =  ndb.StringProperty()
	status =  ndb.StringProperty( choices=( 'Invited','Going','Not going' ) )