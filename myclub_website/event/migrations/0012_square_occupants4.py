# Generated by Django 4.1.7 on 2023-03-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_userprofile2'),
    ]

    operations = [
        migrations.AddField(
            model_name='square',
            name='occupants4',
            field=models.ManyToManyField(blank=True, default=[], to='event.userprofile2'),
        ),
    ]
