from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length=300,  
        help_text="Titre de l'article"
    )
    content = models.TextField(help_text="Contenu de l'article")
    image = models.ImageField(
        upload_to='images/',  
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Date d'envoi

    def __str__(self):
        return f"{self.name} - {self.email}"