# Generated by Django 3.1.3 on 2020-12-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_nota_total_custo'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='data_instante',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
