# Generated by Django 4.1.4 on 2022-12-26 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pesssoa',
            new_name='Pessoa',
        ),
    ]
