# Generated by Django 2.2.9 on 2020-05-13 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200513_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='user',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='bid',
            field=models.CharField(default='abc', max_length=100),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='bookmark',
            field=models.ForeignKey(default='abc', null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Bookmark'),
        ),
    ]