# Generated by Django 5.0.2 on 2024-03-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminFinanceApp', '0002_delete_admin_register'),
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
    ]
