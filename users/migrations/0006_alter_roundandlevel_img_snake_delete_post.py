# Generated by Django 4.0.2 on 2022-04-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roundandlevel',
            name='Img_snake',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
