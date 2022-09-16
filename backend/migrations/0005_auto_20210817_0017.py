# Generated by Django 3.1.7 on 2021-08-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='staf',
            name='contact',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.CharField(default='August 17, 2021', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date_add',
            field=models.CharField(default='August 17, 2021', max_length=1000),
        ),
    ]