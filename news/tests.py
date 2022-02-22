from django.test import TestCase
from .models import Editor,Article,tags

class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.widen= Editor(first_name = 'Widen', last_name ='Ratemo', email ='widen@gmail.com')
    
    # Testing  instance to confirm that the object is being instantiated correctly.
    def test_instance(self):
        self.assertTrue(isinstance(self.widen,Editor))   

    #Testing Save Method
    def test_save_method(self):
        self.widen.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)