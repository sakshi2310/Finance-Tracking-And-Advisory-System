# Generated by Django 5.0.2 on 2024-03-19 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminFinanceApp', '0004_amounttype_expancesource_incomesource'),
        ('FinanceApp', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='Email',
            field=models.CharField(default=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user_register',
            name='Mobile_no',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_register',
            name='Password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user_register',
            name='Username',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.CreateModel(
            name='average',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.CharField(default='', max_length=100)),
                ('incometerm', models.CharField(default='', max_length=100)),
                ('expance', models.CharField(default='', max_length=100)),
                ('expanceterm', models.CharField(default='', max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinanceApp.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='Expance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_type', models.CharField(default='', max_length=100)),
                ('amount', models.CharField(default='', max_length=100)),
                ('date', models.DateTimeField()),
                ('amount_status', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('amount_sourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminFinanceApp.incomesource')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinanceApp.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(default='', max_length=100)),
                ('date', models.DateTimeField()),
                ('amount_status', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('amount_sourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminFinanceApp.incomesource')),
                ('amount_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminFinanceApp.amounttype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinanceApp.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.BigIntegerField(default=0)),
                ('card', models.BigIntegerField(default=0)),
                ('saving', models.BigIntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinanceApp.user_register')),
            ],
        ),
    ]
