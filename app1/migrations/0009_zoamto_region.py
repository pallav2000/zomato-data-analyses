# Generated by Django 2.2 on 2020-06-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20200610_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoamto',
            name='REGION',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
