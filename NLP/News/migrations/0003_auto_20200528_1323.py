# Generated by Django 2.2.10 on 2020-05-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_db',
            name='article_link',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
