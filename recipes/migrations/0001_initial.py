# Generated by Django 3.1 on 2020-08-18 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRecipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=50, null=True)),
                ('description', models.CharField(default=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(default=False, null=True, verbose_name='2020-8-17')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PopularRecipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=50, null=True)),
                ('description', models.CharField(default=True, max_length=500, null=True)),
                ('date_created', models.DateTimeField(verbose_name='2020-8-17')),
            ],
        ),
    ]
