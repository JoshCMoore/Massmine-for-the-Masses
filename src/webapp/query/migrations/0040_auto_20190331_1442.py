# Generated by Django 2.1.7 on 2019-03-31 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0039_auto_20190331_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='utc_offset',
            field=models.CharField(default='utc_offset', max_length=100, null=True),
        ),
    ]
