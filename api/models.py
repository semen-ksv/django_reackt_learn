from django.db import models
import string
import random

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip =models.IntegerField(null=False, default=1)
    create_at = models.DateTimeField(auto_now_add=True)

    def is_host_is(self):
        pass

    def generate_unique_code(self):
        length = 8
        while True:
            code = ''.join(random.choice(string.ascii_lowercase, k=length))
            if self.objects.filter(code=code).count() == 0:
                break
        return code
