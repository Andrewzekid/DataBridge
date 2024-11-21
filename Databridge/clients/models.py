from django.db import models
from core.models import Userprofile
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Client(models.Model):
    """Django class for handling clients"""
    userprofile = models.OneToOneField(Userprofile,related_name="client",on_delete=models.CASCADE)


class Request(models.Model):
    """Django class for handling data requests"""
    name = models.CharField(max_length=256)
    data_amount = models.PositiveIntegerField()
    client = models.ForeignKey(Client,related_name="requests",on_delete=models.SET_NULL)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Request, self).save(*args, **kwargs)
    
class Submission(models.Model):
    """Class for managing submissions"""
    request = models.ForeignKey(Request,related_name="submissions",on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(Userprofile,related_name="submissions",on_delete=models.SET_NULL)
    submitted_at = models.DateTimeField(auto_now_add=True)
    documents = models.FileField()
