from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.urls import reverse 

User = settings.AUTH_USER_MODEL


class Blog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=300)
	desc = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	tags = models.TextField()
	slug = models.SlugField(null=True, blank=True, unique=True)


	def get_absolute_url(self):
		return reverse('blog-detail', kwargs={"slug":self.slug})

	def get_edit_absolute_url(self):
		return reverse('blog-update', kwargs={"slug":self.slug})



def blog_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(blog_pre_save_receiver, sender=Blog)

