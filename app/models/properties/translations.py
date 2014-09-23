from ferris import ndb

# ---- auxiliary models ----

class StringTranslation(ndb.Model):
	spanish = ndb.StringProperty()
	english = ndb.StringProperty()
	portuguese = ndb.StringProperty()

class ChoiceTranslation(ndb.Model):
	spanish = ndb.StringProperty()
	english = ndb.StringProperty()
	portuguese = ndb.StringProperty()



# ---- property definitions ----

class StringTranslationProperty(ndb.StructuredProperty):
	def __init__(self, **kwds ):
		super( StringTranslationProperty, self ).__init__( StringTranslation, **kwds )

class ChoiceTranslationProperty(ndb.StructuredProperty):
	"""Example of usage

		*model definition

			class GeneralEvent(BasicModel):
				title = ChoiceTranslationProperty( spanish_choices=( 'hola','pepino' ),
												   english_choices=( 'hello','cucumber'),
												   portuguese_choices=( 'ajo','toto' ) 
												  )

		*instance creation

			my_event = GeneralEvent( title = ChoiceTranslation( english= 'hello', spanish='hola', portuguese='ajo' ) )

	"""

	def __init__( self, spanish_choices = None, english_choices = None, portuguese_choices = None,  **kwds ):
		self.spanish_choices = spanish_choices
		self.english_choices = english_choices
		self.portuguese_choices = portuguese_choices
		super( ChoiceTranslationProperty, self ).__init__( ChoiceTranslation, **kwds )

	def _validate(self, value):
	    if value.spanish != None:
	    	if not self.exist_in_dictionary( self.spanish_choices, value.spanish ):
	      		raise TypeError('The value %s is not a valid spanish_choice option, possible options are %s ' % (repr(value.spanish),repr(self.spanish_choices)) )
	    if value.english != None:
	    	if not self.exist_in_dictionary( self.english_choices, value.english ):
	      		raise TypeError('The value %s is not a valid english_choice option, possible options are %s ' % (repr(value.english),repr(self.english_choices)) )
	    if value.portuguese != None:
	    	if not self.exist_in_dictionary( self.portuguese_choices, value.portuguese ):
	      		raise TypeError('The value %s is not a valid portuguese_choice option, possible options are %s ' % (repr(value.portuguese),repr(self.portuguese_choices)) )

	def exist_in_dictionary( self, choices_tuple, searched_value ):
		for value in choices_tuple:
			if value == searched_value:
				return True
		return False
