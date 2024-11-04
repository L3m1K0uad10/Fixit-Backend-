# Generated by Django 4.0.10 on 2024-06-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='currency',
            field=models.CharField(choices=[('CFA', 'Franc CFA'), ('USD', 'Dollar'), ('EUR', 'Euro'), ('Rps', 'Roupies'), ('GBP', 'Pound sterling')], default='USD', max_length=16),
        ),
    ]
