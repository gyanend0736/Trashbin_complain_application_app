from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # links complaint to the user
    
    text = models.TextField()
    areacode= models.IntegerField()
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint by {self.user.username}"