# Generated by Django 5.0.6 on 2024-06-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internweb', '0005_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='mob',
            field=models.CharField(default='', max_length=10),
        ),
    ]
