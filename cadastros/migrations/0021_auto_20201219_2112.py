# Generated by Django 3.1.3 on 2020-12-20 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0020_auto_20201219_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotacao',
            name='ativo',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
