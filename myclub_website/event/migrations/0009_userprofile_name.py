# Generated by Django 4.1.7 on 2023-03-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_square_occupants2'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='0', max_length=120, verbose_name='User Name'),
        ),
    ]
