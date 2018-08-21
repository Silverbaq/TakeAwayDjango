# Generated by Django 2.1 on 2018-08-20 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderfood', '0003_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orderfood.Event'),
            preserve_default=False,
        ),
    ]
