# Generated by Django 2.2.9 on 2020-05-14 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20200513_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customerrad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bookmark',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Bookmark'),
        ),
    ]
