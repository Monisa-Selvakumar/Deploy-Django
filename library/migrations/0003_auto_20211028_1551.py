# Generated by Django 3.0 on 2021-10-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_issuedbook_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
