from django.db import models

class Note(models.Model):
    """
    Model representing a Sticky Note.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the Note object.
        """
        return self.title