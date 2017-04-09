from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Dorm(models.Model):
    devID = models.PositiveIntegerField(null=True)
    devName = models.CharField(max_length=4, null=True)
    devStatus = models.PositiveIntegerField(null=True)
    roomName = models.PositiveIntegerField(null=True)
    nRelays = models.PositiveIntegerField(null=True)
    relay = models.CharField(max_length=30, null=True)
    # time = models.DateTimeField(default=timezone.now)
    time = models.DateTimeField(auto_now=True, null=True)

    def getRouter(self):
        """
        Get router.
        """
        if self.nRelays == 1:
            pass
