# Generated by Django 4.0.4 on 2022-12-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('eid', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('sid', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='student_pic')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('u_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
    ]