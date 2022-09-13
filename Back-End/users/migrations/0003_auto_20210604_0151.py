# Generated by Django 3.2 on 2021-06-03 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210603_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='page',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='license',
            name='purchase_id',
            field=models.CharField(default='E7FD15', editable=False, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_id',
            field=models.CharField(default='2C8610', editable=False, max_length=20, primary_key=True, serialize=False),
        ),
    ]
