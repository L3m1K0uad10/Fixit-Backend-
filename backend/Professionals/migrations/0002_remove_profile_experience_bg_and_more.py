# Generated by Django 4.0.10 on 2024-06-15 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Professionals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='experience_bg',
        ),
        migrations.AddField(
            model_name='experiencebackground',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='experience_backgrounds', to='Professionals.profile'),
            preserve_default=False,
        ),
    ]