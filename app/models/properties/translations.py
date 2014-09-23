from ferris import ndb

# ---- auxiliary models ----

class StringTranslation(ndb.Model):
	spanish = ndb.StringProperty()
	english = ndb.StringProperty()
	portuguese = ndb.StringProperty()

class TextTranslation(ndb.Model):
	spanish = ndb.TextProperty()
	english = ndb.TextProperty()
	portuguese = ndb.TextProperty()

class ChoiceTranslation(ndb.Model):
	keyname = ndb.StringProperty()
	spanish = ndb.StringProperty()
	english = ndb.StringProperty()
	portuguese = ndb.StringProperty()



# ---- property definitions ----

class StringTranslationProperty(ndb.StructuredProperty):
	def __init__(self, **kwds ):
		super( StringTranslationProperty, self ).__init__( StringTranslation, **kwds )

class TextTranslationProperty(ndb.StructuredProperty):
	def __init__(self, **kwds ):
		super( TextTranslationProperty, self ).__init__( TextTranslation, **kwds )

class ChoiceTranslationProperty(ndb.StructuredProperty):
	
	#	Definition:
	#		objectProperty = ChoiceTranslationProperty(spanish_choices=( 'hola',... ), english_choices=( 'hello',...),portuguese_choices=( 'ola',... ))
	#	Initialization:
	#		object = Object( title = ChoiceTranslation( english= 'hello', spanish='hola', portuguese='ola'))


	def __init__( self, choices=None,  **kwds ):
		self.choices = choices
		super( ChoiceTranslationProperty, self ).__init__( ChoiceTranslation, **kwds )

	def _validate(self, value):
		if value.keyname != None:
			if not self.exist_in_dictionary( self.choices, value.keyname ):
				raise TypeError('The value %s is not a valid choice option, possible options are %s ' % (repr(value.keyname),repr(self.choices.keys())) )

	def exist_in_dictionary( self, choices, searched_value ):
		for key,value in choices:
			if key == searched_value:
				return True
		return False

	def _to_base_type(self, value):
		spanish = self.choices[value]['spanish']
		english = self.choices[value]['english']
		portuguese = self.choices[value]['portuguese']
		tmodel = ChoiceTranslation( keyname=value, spanish=spanish, english=english, portuguese=portuguese )
		return tmodel
