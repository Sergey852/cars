# Generated by Django 4.1 on 2022-08-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_homeonecolumn_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeonecolumn',
            name='text1',
            field=models.TextField(default=1, verbose_name='Column text1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homethreecolumns',
            name='text1',
            field=models.TextField(default=1, verbose_name='Column text1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hometwocolumns',
            name='text1',
            field=models.TextField(default=1, verbose_name='Column text1'),
            preserve_default=False,
        ),
    ]
