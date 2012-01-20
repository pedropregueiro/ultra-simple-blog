from django.db import models
from django.forms import ModelForm, Textarea

class Post(models.Model):
    title = models.CharField(max_length="200")
    body = models.TextField()
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField(null=True)
    date_deleted = models.DateTimeField(null=True)
		
    def __unicode__(self):
			return self.title
			
			
class PostForm(ModelForm):
	class Meta:
		model = Post
		exclude = ('date_published', 'date_modified', 'date_deleted')

