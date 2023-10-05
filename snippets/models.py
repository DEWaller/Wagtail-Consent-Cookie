from django.db import models
from django.core.exceptions import ValidationError

#from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks


@register_snippet
class CookieConsent(models.Model):
    version = models.IntegerField(default=1)
    title = models.CharField(max_length=50, help_text="Internal use only, not shown on website.")
    message = RichTextField(features=["bold", "h2"])
    accept_button = models.CharField(max_length=50)
    decline_button = models.CharField(max_length=50)
    categories = StreamField([
        ('category', blocks.StructBlock([
            ('name', blocks.CharBlock(help_text="If changed the template will need updating.")),
            ('description', blocks.TextBlock()),
        ]))
    ], use_json_field=True, null=True, blank=True)

    panels = [
        FieldPanel('version'),
        FieldPanel('title'),
        FieldPanel('message'),
        FieldPanel('accept_button'),
        FieldPanel('decline_button'),
        FieldPanel('categories'),
    ]
    
    def save(self, *args, **kwargs):
        if not self.pk and CookieConsent.objects.exists():
            raise ValidationError('There is already an instance of CookieConsent')
        return super(CookieConsent, self).save(*args, **kwargs)

    def __str__(self):
        return self.title