# Generated by Django 4.1.7 on 2023-04-13 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_feed_like_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='is_liked',
            new_name='is_like',
        ),
    ]