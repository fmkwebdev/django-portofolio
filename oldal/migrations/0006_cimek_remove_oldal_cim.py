# Generated by Django 4.1.4 on 2022-12-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oldal', '0005_oldal_delete_cim_delete_hatter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cimek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cim', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='oldal',
            name='cim',
        ),
    ]
