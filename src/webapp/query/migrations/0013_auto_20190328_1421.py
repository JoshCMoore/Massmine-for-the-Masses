# Generated by Django 2.1.7 on 2019-03-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0012_auto_20190328_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.CharField(default='created_at', max_length=100),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id_str',
            field=models.CharField(default='tweet_id_str', max_length=100),
        ),
    ]
