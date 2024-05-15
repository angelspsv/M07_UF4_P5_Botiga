# Generated by Django 5.0.3 on 2024-05-14 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrito', '0002_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('id_carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.carrito')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
        ),
    ]