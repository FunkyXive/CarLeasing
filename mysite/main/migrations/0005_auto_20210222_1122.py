# Generated by Django 3.0.5 on 2021-02-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210216_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='carNewPrice',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='cvrNumber',
            field=models.IntegerField(),
        ),
    ]
