# Generated by Django 3.1.3 on 2020-11-10 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_purchase_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='category',
        ),
    ]
