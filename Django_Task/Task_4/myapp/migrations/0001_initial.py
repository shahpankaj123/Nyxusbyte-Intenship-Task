# Generated by Django 5.0 on 2023-12-16 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
