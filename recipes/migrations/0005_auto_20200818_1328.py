# Generated by Django 3.1 on 2020-08-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200818_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrecipes',
            name='description',
            field=models.CharField(default=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='popularrecipes',
            name='description',
            field=models.CharField(default=True, max_length=2000, null=True),
        ),
    ]
