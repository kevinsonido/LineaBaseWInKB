# Generated by Django 4.1.2 on 2022-10-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LineaBaseApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialescaneo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]