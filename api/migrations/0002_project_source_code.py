# Generated by Django 3.0.2 on 2020-02-04 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='source_code',
            field=models.TextField(blank=True, max_length=360),
        ),
    ]