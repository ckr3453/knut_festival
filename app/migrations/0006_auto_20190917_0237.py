# Generated by Django 2.2.5 on 2019-09-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_board_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
