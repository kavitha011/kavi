# Generated by Django 5.2.1 on 2025-05-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_biodata_rename_address_hospital_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='mobile_no',
            field=models.CharField(max_length=20),
        ),
    ]
