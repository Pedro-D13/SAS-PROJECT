# Generated by Django 2.1.4 on 2019-07-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
