# Generated by Django 3.1.3 on 2020-12-06 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_auto_20201205_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='Lucro_Day_Trade',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.01, max_digits=10, verbose_name='Lucro Day Trade'),
        ),
    ]