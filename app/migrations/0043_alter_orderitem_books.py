# Generated by Django 4.1.7 on 2023-02-16 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='Books',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_order', to='app.books'),
        ),
    ]
