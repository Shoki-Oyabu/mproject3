# Generated by Django 3.2.16 on 2023-01-19 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_auto_20230118_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('stocks_visited', models.ManyToManyField(to='myapp.Stock')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
