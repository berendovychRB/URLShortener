# Generated by Django 3.1.1 on 2020-09-23 09:42

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20200922_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url]),
        ),
    ]
