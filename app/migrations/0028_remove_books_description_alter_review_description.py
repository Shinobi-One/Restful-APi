# Generated by Django 4.1.2 on 2023-02-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_review_description_alter_books_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='description',
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thoughts', to='app.books'),
        ),
    ]