# Generated by Django 3.1.3 on 2020-12-06 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_nota_data_instante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='IRRF_Day_Trade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='IRRF Day Trade'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='IRRF_Final',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='IRRF Final'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='Lucro_Day_Trade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Lucro Day Trade'),
        ),
    ]
