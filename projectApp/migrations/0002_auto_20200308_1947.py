# Generated by Django 3.0.4 on 2020-03-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image_uploader',
            old_name='file',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='image_uploader',
            name='id',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
    ]