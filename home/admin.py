from django.contrib import admin
from home.models import Carousel, Team, Services, ServicesItems, NewIdeas, NewIdeasItems, Testemonial, TestemonialsItems, Contact, NewsLetter
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Carousel)
admin.site.register(Team)
admin.site.register(Services)
admin.site.register(ServicesItems)
admin.site.register(NewIdeas)
admin.site.register(NewIdeasItems)
admin.site.register(Testemonial)
admin.site.register(TestemonialsItems)
admin.site.register(Contact)
admin.site.register(NewsLetter)