# Generated by Django 3.1.3 on 2020-12-22 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0023_nota_usuer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.CharField(max_length=250)),
                ('tipo_provento', models.CharField(choices=[('D', 'DIVIDENDOS'), ('J', 'JUROS COMPOSTO')], max_length=250)),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
