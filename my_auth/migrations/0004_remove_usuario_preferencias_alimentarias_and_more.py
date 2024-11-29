# Generated by Django 5.1.3 on 2024-11-28 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0003_alter_usuario_altura_alter_usuario_peso'),
        ('preferencias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='preferencias_alimentarias',
        ),
        migrations.AddField(
            model_name='usuario',
            name='preferencias_alimentarias',
            field=models.ManyToManyField(blank=True, to='preferencias.preferenciaalimentaria'),
        ),
    ]