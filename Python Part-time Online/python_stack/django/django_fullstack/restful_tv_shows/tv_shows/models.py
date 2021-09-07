from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['title'])<2:
            errors["title"]="Title should be at least 2 characters"
        if len(postData['network'])<2:
            errors["network"]="Network should be at least 3 characters"
        if len(postData['release_date'])==None:
            errors["release_date"]="Release Date required"
        if len(postData['description'])<10:
            errors["description"]="Description should be at least 10 characters"
        return errors

class Show (models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager()

    def __repr__(self):
        return f"<Show: {self.title} ({self.release_date}) ({self.id})>"