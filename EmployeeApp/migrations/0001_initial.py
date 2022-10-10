# Generated by Django 4.1.2 on 2022-10-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departements',
            fields=[
                ('DepartementId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartementName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=500)),
                ('Departement', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
                ('PhotoName', models.CharField(max_length=500)),
            ],
        ),
    ]
