# Generated by Django 3.2.19 on 2024-10-22 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
