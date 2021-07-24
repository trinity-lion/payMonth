# Generated by Django 3.2.5 on 2021-07-24 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210724_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('Entertainment', 'Entertainment'), ('Shopping', 'Shopping'), ('Program', 'Program'), ('Game', 'Game'), ('Etc', 'Etc')], default='Entertainment', max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='pay_interval',
            field=models.CharField(choices=[('month', 'month'), ('quarter', 'quarter'), ('half', 'half'), ('yearly', 'yearly')], default='month', max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='shared',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=100),
        ),
    ]
