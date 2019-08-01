# Generated by Django 2.2.3 on 2019-07-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0003_farmerproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='milk',
            name='milk_id',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='country_code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='milk',
            name='milk_company_category_id',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(unique=True),
        ),
    ]