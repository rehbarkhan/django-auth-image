from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(_("Created date and time"), auto_now_add = True)
    updated_on = models.DateTimeField(_("Updated date and time"), auto_now = True)


class VideoFile(models.Model):
    uploaded_by = models.ForeignKey(User, related_name='VideoFile', on_delete=models.CASCADE)
    video_file = models.FileField(_("Video File"), upload_to='video')

class VideoDescription(BaseModel):
    created_by = models.ForeignKey(User, related_name='VideoDescription', on_delete=models.CASCADE)
    video_file = models.OneToOneField(VideoFile, related_name='VideoDescription', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return str(self.title)