# Generated by Django 3.0.6 on 2020-06-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_userorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorder',
            name='order',
        ),
        migrations.AddField(
            model_name='userorder',
            name='order',
            field=models.ManyToManyField(blank=True, to='orders.UserCart'),
        ),
    ]
