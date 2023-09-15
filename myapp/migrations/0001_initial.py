# Generated by Django 4.2.3 on 2023-07-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=150)),
                ('occupation', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('age', models.BigIntegerField(default=0)),
                ('thumb', models.ImageField(default='default.png', upload_to='')),
            ],
        ),
    ]