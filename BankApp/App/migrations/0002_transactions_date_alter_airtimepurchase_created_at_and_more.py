# Generated by Django 5.1.7 on 2025-05-15 14:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='airtimepurchase',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='billpayment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='type',
            field=models.CharField(choices=[('deposit', 'Deposit'), ('transfer', 'Transfer'), ('withdrawal', 'Withdrawal')], max_length=20),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
