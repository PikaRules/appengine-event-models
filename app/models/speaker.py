from ferris import BasicModel, ndb

class Speaker(BasicModel):
	event_person_id = ndb.IntegerProperty(required=True)
	market_place_person_id = ndb.IntegerProperty()
	first_name = ndb.StringProperty()
	last_name = ndb.StringProperty()
	picture_url = ndb.StringProperty()
	email =  ndb.StringProperty()
	facebook_account = ndb.StringProperty()
	linkedin_account = ndb.StringProperty()
	twitter_account =  ndb.StringProperty()
	biography = ndb.StringProperty()
	biography_url = ndb.StringProperty()
	company =  ndb.StringProperty()