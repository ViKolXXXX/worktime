# Generated by Django 2.1.7 on 2019-04-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igbrv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loadteacher',
            old_name='y33',
            new_name='y34',
        ),
        migrations.AddField(
            model_name='loadteacher',
            name='y98',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loadteacher',
            name='y1',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loadteacher',
            name='y3',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loadteacher',
            name='y31',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loadteacher',
            name='y41',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loadteacher',
            name='y49',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loadteacher',
            name='y5',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loadteacher',
            name='y71',
            field=models.FloatField(default=0, null=True),
        ),
    ]
