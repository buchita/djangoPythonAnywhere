# Generated by Django 3.0.4 on 2020-03-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projectApp', '0005_delete_flower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('description', models.CharField(default='please add description', max_length=2000)),
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.TextField(null=True)),
            ],
            options={
                'db_table': 'flower',
            },
        ),
    ]
