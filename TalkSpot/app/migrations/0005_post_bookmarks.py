# Generated by Django 5.1.5 on 2025-02-16 12:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
