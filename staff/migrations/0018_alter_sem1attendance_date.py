# Generated by Django 4.0.4 on 2022-07-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0017_alter_sem1attendance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sem1attendance',
            name='date',
            field=models.DateField(),
        ),
    ]
