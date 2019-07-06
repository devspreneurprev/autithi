# Generated by Django 2.1.5 on 2019-07-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20190706_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='object_id',
        ),
        migrations.AddField(
            model_name='notification',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
