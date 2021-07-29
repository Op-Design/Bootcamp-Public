from django.db import models
from django.db.models.fields import DateField

class Dojo (models.Model):
    # Id automatically create
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    desc=models.CharField(max_length=255)
    # ninja = associated ninjas in a given dojo

    def __repr__(self):
        return f"<Dojo: {self.name} ({self.id})>"

class Ninja (models.Model):
    # Id automatically create
    dojo = models.ForeignKey(Dojo, related_name="ninja", on_delete=models.CASCADE)
    # dojo is actually record as "dojo_id" in the database
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Ninja: {self.first_name} {self.last_name} ({self.id})>"