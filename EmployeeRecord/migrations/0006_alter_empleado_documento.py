# Generated by Django 3.2.5 on 2021-10-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeRecord', '0005_auto_20211013_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='Documento',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
