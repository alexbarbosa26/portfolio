# Generated by Django 3.1.3 on 2020-12-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0015_auto_20201214_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotacao',
            name='data_instante',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cotacao',
            name='fechamento_ajustado',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
