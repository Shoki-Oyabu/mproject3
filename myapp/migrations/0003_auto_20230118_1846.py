# Generated by Django 3.2.16 on 2023-01-18 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_stocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tick', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('IPO', models.CharField(max_length=200)),
                ('sector', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Stocks',
        ),
    ]
