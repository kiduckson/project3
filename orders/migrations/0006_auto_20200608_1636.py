# Generated by Django 3.0.6 on 2020-06-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200608_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinnerplatter',
            name='size',
            field=models.CharField(choices=[('L', 'Large'), ('S', 'Small')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('L', 'Large'), ('S', 'Small')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='sub',
            name='size',
            field=models.CharField(choices=[('L', 'Large'), ('S', 'Small')], default='S', max_length=1),
        ),
    ]
