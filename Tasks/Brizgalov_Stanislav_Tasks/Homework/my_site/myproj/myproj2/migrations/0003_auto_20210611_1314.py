# Generated by Django 3.2.3 on 2021-06-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproj2', '0002_auto_20210611_1215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Posts', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
