from django.db import models

# Create your models here.

class Publisher(models.Model):    
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50);
    website = models.URLField();
    num_pages = models.IntegerField(blank = True, null = True)
    


    def __str__(self):
        return self.name;

    class Admin:
        pass;
    
class Author(models.Model):
    salutation = models.CharField(max_length = 10)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='/tmp')

    def __str__(self):
        return "{firstName} {lastName}".format(firstName = first_name, lastName = last_name);

    class Admin:
         pass;
        
class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title;

    class Admin:
        pass;
