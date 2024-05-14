# Generated by Django 4.2.4 on 2024-05-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('primer_apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('segundo_apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='usuarios_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='usuarios_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
