# Generated by Django 5.1.3 on 2024-11-30 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0005_usuario_imc_usuario_macronutrientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
