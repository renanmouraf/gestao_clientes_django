# Generated by Django 2.0.1 on 2018-08-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20180829_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]