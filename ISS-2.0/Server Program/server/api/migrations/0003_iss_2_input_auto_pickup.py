# Generated by Django 4.2.1 on 2023-06-03 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_iss_2_input_id_alter_iss_2_input_md5'),
    ]

    operations = [
        migrations.AddField(
            model_name='iss_2_input',
            name='auto_pickup',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]