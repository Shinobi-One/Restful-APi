# Generated by Django 4.1.2 on 2023-01-30 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_collection_num_stuff1_collectioner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuff1',
            name='collectioner',
        ),
        migrations.AddField(
            model_name='collection',
            name='collectioner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.stuff1'),
        ),
    ]