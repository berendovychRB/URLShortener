# Generated by Django 3.1.1 on 2020-09-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20200922_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]