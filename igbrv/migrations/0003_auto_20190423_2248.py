# Generated by Django 2.1.7 on 2019-04-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igbrv', '0002_auto_20190422_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadteacher',
            name='all_sum',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='loadteacher',
            name='sum_f',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='loadteacher',
            name='sum_g',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='loadteacher',
            name='sum_y',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='loadteacher',
            name='sum_z',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
