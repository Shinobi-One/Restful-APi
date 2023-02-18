# Generated by Django 4.1.7 on 2023-02-16 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_remove_order_items_cartitem_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='items',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(null=True)),
                ('Books', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.books')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='app.order')),
            ],
        ),
    ]
