# Generated by Django 4.1.2 on 2023-02-05 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_review_title_review_review_num_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='titleReview',
        ),
    ]