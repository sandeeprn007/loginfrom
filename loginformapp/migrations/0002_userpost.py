# Generated by Django 4.1.2 on 2023-01-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginformapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Subtitle', models.CharField(max_length=200)),
                ('Subj', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='images/')),
                ('Created_By', models.CharField(max_length=200)),
            ],
        ),
    ]