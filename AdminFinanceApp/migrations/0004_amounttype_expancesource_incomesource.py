# Generated by Django 5.0.2 on 2024-03-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminFinanceApp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amounttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expancesource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourse', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Incomesource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourse', models.CharField(max_length=100)),
            ],
        ),
    ]
