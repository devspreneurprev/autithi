# Generated by Django 2.1.5 on 2019-05-17 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0003_auto_20190517_1209'),
        ('accounts', '0002_auto_20190407_1539'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_by_user', models.BooleanField(default=True)),
                ('request_accepted_by_host', models.BooleanField(default=True)),
                ('requested_at', models.DateField(auto_now_add=True)),
                ('request_accepted_at', models.DateField(auto_now_add=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Host')),
                ('proparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Proparty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
