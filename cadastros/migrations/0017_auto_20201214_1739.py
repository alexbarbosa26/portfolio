# Generated by Django 3.1.3 on 2020-12-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0016_auto_20201214_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotacao',
            name='data_instante',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]