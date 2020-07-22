# Generated by Django 3.0.7 on 2020-07-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codelists', '0003_auto_20200628_0923'),
        ('opencodelists', '0002_auto_20200424_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codelist',
            name='csv_data',
            field=models.TextField(null=True, verbose_name='CSV data'),
        ),
        migrations.AlterField(
            model_name='codelist',
            name='version_str',
            field=models.CharField(max_length=12, null=True, verbose_name='Version'),
        ),
    ]
