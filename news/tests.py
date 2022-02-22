from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

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
class ArticleTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.mary= Editor(first_name = 'Mary', last_name ='John', email ='mary@moringaschool.com')
        self.mary.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()
        
        #Since the Editor and Article share a One to Many relationship we have to save the editor instance first then equate it to the editor field in the Article model.
        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.mary)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
        
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)
        
    def test_get_news_by_date(self):
        test_date = '2022-02-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)