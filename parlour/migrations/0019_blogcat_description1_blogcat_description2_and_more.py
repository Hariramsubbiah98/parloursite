# Generated by Django 5.0.3 on 2024-06-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlour', '0018_blogcat_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcat',
            name='description1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogcat',
            name='description2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogcat',
            name='description_title1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogcat',
            name='description_title2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
