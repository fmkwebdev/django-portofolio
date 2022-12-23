# Generated by Django 4.1.4 on 2022-12-13 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oldal', '0003_alter_oldal_hatter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('focim', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hatter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hatter', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Oldal',
        ),
    ]
