# Generated by Django 3.2.9 on 2021-11-07 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='categoy',
            new_name='category',
        ),
    ]
