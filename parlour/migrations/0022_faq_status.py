# Generated by Django 5.0.3 on 2024-06-21 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlour', '0021_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='status',
            field=models.BooleanField(default=False, help_text='0-Available 1-Suspended'),
        ),
    ]
