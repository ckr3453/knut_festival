# Generated by Django 2.2.5 on 2019-09-23 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_board_page_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendsboard',
            name='page_counter',
            field=models.BigIntegerField(default=0),
        ),
    ]
