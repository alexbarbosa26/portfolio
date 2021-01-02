# Generated by Django 3.1.3 on 2020-12-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_nota_total_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='total_custo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Total Compra'),
        ),
    ]
