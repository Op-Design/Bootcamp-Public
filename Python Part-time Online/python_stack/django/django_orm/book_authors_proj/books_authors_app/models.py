from django.db import models

class Book(models.Model):
    # Id automatically create
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # author = associated author

    def __repr__(self):
        return f"<Book: {self.title} {self.desc} ({self.id})>"

class Author(models.Model):
    # Id automatically create
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="author")
    notes = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Users: {self.first_name} {self.last_name} ({self.id})>"