# Generated by Django 3.0 on 2019-12-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gal', '0002_image_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_name']},
        ),
        migrations.AlterField(
            model_name='image',
            name='image_description',
            field=models.TextField(),
        ),
    ]
