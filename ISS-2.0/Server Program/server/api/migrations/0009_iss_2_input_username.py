# Generated by Django 4.2.1 on 2023-06-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_iss_2_input_auto_pickup'),
    ]

    operations = [
        migrations.AddField(
            model_name='iss_2_input',
            name='username',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
