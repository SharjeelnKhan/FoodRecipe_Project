# Generated by Django 3.1 on 2020-08-20 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_auto_20200819_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrecipes',
            name='description',
            field=models.CharField(default=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customerrecipes',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customerrecipes',
            name='ingredients',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='customerrecipes',
            name='instructions',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='customerrecipes',
            name='level',
            field=models.CharField(default=False, max_length=25),
        ),
        migrations.AlterField(
            model_name='customerrecipes',
            name='name',
            field=models.CharField(default=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customerrecipes',
            name='time_needed',
            field=models.CharField(default=False, max_length=25),
        ),
    ]