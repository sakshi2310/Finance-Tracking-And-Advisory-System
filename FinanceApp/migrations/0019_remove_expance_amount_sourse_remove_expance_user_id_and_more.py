# Generated by Django 5.0 on 2024-03-22 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceApp', '0018_goals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expance',
            name='amount_sourse',
        ),
        migrations.RemoveField(
            model_name='expance',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='goals',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='income',
            name='amount_sourse',
        ),
        migrations.RemoveField(
            model_name='income',
            name='amount_type',
        ),
        migrations.RemoveField(
            model_name='income',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='personal_info',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='average',
        ),
        migrations.DeleteModel(
            name='Expance',
        ),
        migrations.DeleteModel(
            name='Goals',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
        migrations.DeleteModel(
            name='Personal_info',
        ),
        migrations.DeleteModel(
            name='User_Register',
        ),
    ]
