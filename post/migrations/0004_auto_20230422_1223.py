# Generated by Django 3.1 on 2023-04-22 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20230422_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='angry',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='disgust',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='fear',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='happy',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='neutral',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='sad',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='surprise',
            field=models.FloatField(default=0),
        ),
    ]