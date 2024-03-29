# Generated by Django 5.0 on 2024-03-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminFinanceApp', '0005_delete_admin_register_delete_amounttype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(default='', max_length=200)),
                ('Email', models.CharField(default='', max_length=200, unique=True)),
                ('Password', models.CharField(default='', max_length=200)),
            ],
        ),
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
