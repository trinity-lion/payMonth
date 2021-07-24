# Generated by Django 3.2.3 on 2021-07-24 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('OTT', 'OTT'), ('Music', 'Music'), ('Shopping', 'Shopping'), ('Etc', 'Etc')], max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='pay_interval',
            field=models.CharField(choices=[('month', 'month'), ('quarter', 'quarter'), ('half', 'half'), ('yearly', 'yearly')], max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='shared',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=100),
        ),
    ]