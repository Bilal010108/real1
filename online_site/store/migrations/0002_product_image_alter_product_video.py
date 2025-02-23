# Generated by Django 5.1.2 on 2024-10-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='vid/'),
        ),
    ]
