# Generated by Django 5.0.6 on 2024-07-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(max_length=50, upload_to=''),
        ),
    ]
