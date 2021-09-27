# Generated by Django 3.2.7 on 2021-09-26 14:36

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_appuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='password',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=20)),
        ),
    ]