# Generated by Django 3.1.3 on 2020-11-10 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_budget_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
