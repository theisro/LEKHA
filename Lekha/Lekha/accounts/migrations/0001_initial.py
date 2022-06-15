# Generated by Django 4.0.4 on 2022-06-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('aword1', models.CharField(max_length=200)),
                ('aword2', models.CharField(max_length=200)),
                ('aword3', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=200)),
                ('insta_handle', models.CharField(max_length=200)),
                ('fb_handle', models.CharField(max_length=200)),
                ('twitter_handle', models.CharField(max_length=200)),
                ('private', models.BooleanField(max_length=200)),
            ],
        ),
    ]