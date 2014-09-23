from ferris import ndb



class StringTranslationModel(ndb.Model):
	spanish = ndb.StringProperty()
	english = ndb.StringProperty()
	portuguese = ndb.StringProperty()

class ChoiceTranslationModel(ndb.Model):
	spanish = None
	english = None
	portuguese = None

	def __init__(self, **kwds):
		#spanish_choices = kwds['spanish_choices']
		#english_choices = kwds['english_choices']
		#portuguese_choices = kwds['portuguese_choices']
		if not ( spanish_choices == None):
			self.spanish = ndb.StringProperty( choices=spanish_choices )
		if not ( english_choices == None):
			self.english = ndb.StringProperty( choices=english_choices )
		if not ( portuguese_choices == None):
			self.portuguese = ndb.StringProperty( choices=portuguese_choices )







class StringTranslationProperty(ndb.StructuredProperty):
	def __init__(self, **kwds ):
		super(StringTranslationProperty, self).__init__(StringTranslationModel, **kwds)

class ChoiceTranslationProperty(ndb.StructuredProperty):
	_hola = 'hola'
	def __init__(self,  **kwds ):
		super(ChoiceTranslationProperty, self).__init__(ChoiceTranslationModel, **kwds)

	def _validate(self, value):
	    if value.spanish != self._hola:
	      raise TypeError('expected an value hola, got %s' % repr(value.spanish))

