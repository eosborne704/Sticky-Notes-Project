from django.db import models

# Create your models here.
class Note(models.Model):
    """
    This is how each note should act
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_assigned = models.DateTimeField(auto_now_add=True)

    # Define a ForeignKey for the author's relationship
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title

class User(models.Model):
    """
    Docstring for Author
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
