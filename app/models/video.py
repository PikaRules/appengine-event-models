from ferris import BasicModel, ndb

class Video(BasicModel):
	resource_id = ndb.IntegerProperty(required=True)
	title = ndb.StringProperty()
	description = ndb.StringProperty()
	url_where_to_donwload = ndb.StringProperty()
	thumbnail_url =  ndb.StringProperty()
	extension =  ndb.StringProperty( choices=( 'mp4','mkv','avi','flv' ) )