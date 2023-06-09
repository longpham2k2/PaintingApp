# Generated by Django 4.1.4 on 2023-05-18 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('painting', '0005_userlikepainting_remove_painting_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikepainting',
            name='painting_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painting.painting'),
        ),
        migrations.AlterField(
            model_name='userlikepainting',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
