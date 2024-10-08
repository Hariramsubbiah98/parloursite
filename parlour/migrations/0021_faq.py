# Generated by Django 5.0.3 on 2024-06-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlour', '0020_blogcat_about_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=50)),
                ('answers', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=20)),
            ],
        ),
    ]
