# Generated by Django 3.2.16 on 2023-01-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_accountholder_num_shares'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountholder',
            name='shares',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
