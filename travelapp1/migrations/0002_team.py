# Generated by Django 3.2.13 on 2022-05-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
