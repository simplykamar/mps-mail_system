# Generated by Django 2.2.2 on 2019-09-05 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('tel', models.CharField(max_length=10)),
                ('pic', models.ImageField(default='profile/profile_pic/profile_img.jpg', upload_to='profile/profile_pic')),
                ('type', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], default='Student', max_length=10)),
                ('security', models.CharField(default='', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
