# Generated by Django 5.0.9 on 2024-11-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0004_remove_usuario_preferencias_alimentarias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='macronutrientes',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
