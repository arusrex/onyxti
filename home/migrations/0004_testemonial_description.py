# Generated by Django 5.0.6 on 2024-06-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_newideasitems_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='testemonial',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]