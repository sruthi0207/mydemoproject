# Generated by Django 3.2.4 on 2021-07-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0006_alter_rest_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest',
            name='img',
            field=models.ImageField(upload_to='profile_img/'),
        ),
    ]
