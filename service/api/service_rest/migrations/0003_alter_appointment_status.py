# Generated by Django 4.0.3 on 2023-04-26 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0002_appointment_is_vip_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='In progress', max_length=10),
        ),
    ]
