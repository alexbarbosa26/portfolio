# Generated by Django 3.1.3 on 2020-12-28 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0029_auto_20201228_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='corretora',
        ),
    ]
