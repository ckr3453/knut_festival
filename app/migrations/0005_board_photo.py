# Generated by Django 2.2.5 on 2019-09-16 15:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
