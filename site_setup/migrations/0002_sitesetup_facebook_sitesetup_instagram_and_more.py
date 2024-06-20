# Generated by Django 5.0.6 on 2024-06-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='tiktok',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='x_twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetup',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetup',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetup',
            name='site_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
