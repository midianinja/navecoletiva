# Generated by Django 2.2.7 on 2019-11-09 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0002_auto_20191109_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='rede',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rede.Rede'),
        ),
    ]
