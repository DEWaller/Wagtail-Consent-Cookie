# Generated by Django 4.2.6 on 2023-10-05 15:30

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CookieConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=1)),
                ('title', models.CharField(help_text='Internal use only, not shown on website.', max_length=50)),
                ('message', wagtail.fields.RichTextField()),
                ('accept_button', models.CharField(max_length=50)),
                ('decline_button', models.CharField(max_length=50)),
                ('categories', wagtail.fields.StreamField([('category', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='If changed the template will need updating.')), ('description', wagtail.blocks.TextBlock())]))], blank=True, null=True, use_json_field=True)),
            ],
        ),
    ]