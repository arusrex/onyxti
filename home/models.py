from django.db import models

class Carousel(models.Model):
    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = 'Carousels'

    image = models.ImageField(upload_to='carousel/%Y/%m/%d')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    image = models.ImageField(upload_to='team/%Y/%m/%d')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    short = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Services(models.Model):
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    title = models.CharField(max_length=255)
    description = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class ServicesItems(models.Model):
    class Meta:
        verbose_name = "Service Item"
        verbose_name_plural = "Services Items"

    image = models.ImageField(upload_to='services/%Y/%m/%d')
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class NewIdeas(models.Model):
    class Meta:
        verbose_name = "New Idea"
        verbose_name_plural = "New Ideas"

    title = models.CharField(max_length=255)
    description = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class NewIdeasItems(models.Model):
    class Meta:
        verbose_name = "New Idea Item"
        verbose_name_plural = "New Ideas Items"

    image = models.ImageField(upload_to='new_ideas/%Y/%m/%d')
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Testemonial(models.Model):
    class Meta:
        verbose_name = "Testemonial"
        verbose_name_plural = "Testemonials"

    image = models.ImageField(upload_to='new_ideas/%Y/%m/%d')
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class TestemonialsItems(models.Model):
    class Meta:
        verbose_name = "Testemonial"
        verbose_name_plural = "Testemonials"

    image = models.ImageField(upload_to='testemonial/%Y/%m/%d')
    name = models.CharField(max_length=255)
    call = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class NewsLetter(models.Model):
    class Meta:
        verbose_name = "News Letter"
        verbose_name_plural = "News Letters"

    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    