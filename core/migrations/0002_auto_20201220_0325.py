# Generated by Django 3.1.3 on 2020-12-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]