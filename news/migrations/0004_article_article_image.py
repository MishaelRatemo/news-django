# Generated by Django 4.0.2 on 2022-02-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_editor_phone_number_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(null=True, upload_to='articles/'),
        ),
    ]
