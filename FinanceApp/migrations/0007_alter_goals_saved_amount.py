# Generated by Django 5.0 on 2024-03-21 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceApp', '0006_alter_goals_saved_amount_alter_goals_target_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='Saved_amount',
            field=models.CharField(max_length=200),
        ),
    ]
