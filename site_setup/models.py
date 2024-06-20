from django.db import models

class SiteSetup(models.Model):
    class Meta:
        verbose_name = "Site Setup"
        verbose_name_plural = "Site Setups"

    show_logo = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_header = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_carousel = models.BooleanField(default=True)
    show_team = models.BooleanField(default=True)
    show_services = models.BooleanField(default=True)
    show_new_ideas = models.BooleanField(default=True)
    show_testemonial = models.BooleanField(default=True)
    show_contact = models.BooleanField(default=True)
    show_newsletter = models.BooleanField(default=True)
    show_socials = models.BooleanField(default=True)

    site_name = models.CharField(max_length=100)
    site_description = models.TextField()
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    favicon = models.ImageField(upload_to='favicons/%y/%m/%d', blank=True, null=True)
    logo = models.ImageField(upload_to='logos/%y/%m/%d', blank=True, null=True)
    logo2 = models.ImageField(upload_to='logos/%y/%m/%d', blank=True, null=True)



    def __str__(self):
        return self.site_name
    
