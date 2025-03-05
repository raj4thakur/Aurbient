from django.db import models

class Query(models.Model):
    name = models.CharField(max_length=100)  # User's name
    email = models.EmailField()             # User's email
    message = models.TextField()            # User's query or message
    submitted_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.name
