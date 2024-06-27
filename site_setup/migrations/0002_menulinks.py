# Generated by Django 5.0.6 on 2024-06-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('url', models.URLField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Menu Link',
                'verbose_name_plural': 'Menus Links',
            },
        ),
    ]
