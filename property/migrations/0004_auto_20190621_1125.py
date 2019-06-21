# Generated by Django 2.2 on 2019-06-21 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20190517_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proparty',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propartys', to='city.City'),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propartys', to='accounts.Host'),
        ),
    ]
