# Generated by Django 2.2.10 on 2020-03-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_DB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_link', models.CharField(max_length=500)),
                ('article_title', models.CharField(max_length=500)),
                ('article_timestamp', models.CharField(max_length=150)),
                ('article_intro', models.TextField()),
                ('article_body', models.TextField()),
            ],
        ),
    ]
