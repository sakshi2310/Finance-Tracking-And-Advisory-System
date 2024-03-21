# Generated by Django 5.0 on 2024-03-21 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminFinanceApp', '0004_amounttype_expancesource_incomesource'),
        ('FinanceApp', '0015_remove_expance_amount_sourse_remove_expance_user_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='', max_length=200)),
                ('Email', models.CharField(default=True, max_length=200, unique=True)),
                ('Mobile_no', models.BigIntegerField(default=0)),
                ('Password', models.CharField(default='', max_length=200)),
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
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Goal_name', models.CharField(max_length=200)),
                ('Target_amount', models.BigIntegerField()),
                ('Saved_amount', models.BigIntegerField()),
                ('Targe_date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinanceApp.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='Expance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_type', models.CharField(default='', max_length=100)),
                ('amount', models.BigIntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('amount_status', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('amount_sourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminFinanceApp.incomesource')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinanceApp.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='average',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.BigIntegerField(default=0)),
                ('incometerm', models.CharField(default='', max_length=100)),
                ('expance', models.BigIntegerField(default=0)),
                ('expanceterm', models.CharField(default='', max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinanceApp.user_register')),
            ],
        ),
    ]
