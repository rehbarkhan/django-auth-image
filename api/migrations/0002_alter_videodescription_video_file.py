# Generated by Django 4.2.2 on 2023-11-14 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videodescription',
            name='video_file',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='VideoDescription', to='api.videofile'),
        ),
    ]
