# Generated by Django 4.1.4 on 2022-12-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oldal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cim', models.CharField(max_length=200)),
                ('hatter', models.ImageField(upload_to='')),
            ],
        ),
    ]
