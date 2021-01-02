# Generated by Django 3.1.3 on 2020-12-25 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0025_proventos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.CharField(max_length=250)),
                ('quantidade', models.IntegerField()),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço Total')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
