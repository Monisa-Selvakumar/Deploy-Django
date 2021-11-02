# Generated by Django 3.0 on 2021-10-26 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('issued_date', models.DateField(auto_now=True)),
                ('expiry_date', models.DateField(default=library.models.expiry)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('roll_no', models.CharField(blank=True, max_length=3)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
