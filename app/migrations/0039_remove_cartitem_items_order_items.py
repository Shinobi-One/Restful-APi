# Generated by Django 4.1.7 on 2023-02-16 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_cartitem_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.cartitem'),
        ),
    ]
