# Generated by Django 3.2 on 2021-06-03 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210604_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='purchase_id',
            field=models.CharField(default='16f6a5ebd9844e9591be', editable=False, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_id',
            field=models.CharField(default='025018d7278b4a4ab811', editable=False, max_length=20, primary_key=True, serialize=False),
        ),
    ]
