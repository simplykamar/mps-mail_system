# Generated by Django 2.2.2 on 2019-09-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_auto_20190907_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentmail',
            name='attach',
            field=models.FileField(blank=True, default='', upload_to='attach_data/'),
        ),
    ]