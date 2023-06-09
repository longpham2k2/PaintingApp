# Generated by Django 4.1.4 on 2023-05-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painting', '0004_painting_like_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLikePainting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('painting_id', models.BigIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='painting',
            name='like_count',
        ),
    ]
