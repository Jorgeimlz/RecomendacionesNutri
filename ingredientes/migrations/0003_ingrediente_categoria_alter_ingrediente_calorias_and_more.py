# Generated by Django 5.1.3 on 2024-11-28 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('ingredientes', '0002_ingrediente_calorias_ingrediente_carbohidratos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediente',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredientes', to='categorias.categoria'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='calorias',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='carbohidratos',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='grasas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='proteinas',
            field=models.FloatField(),
        ),
    ]