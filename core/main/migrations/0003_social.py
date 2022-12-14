# Generated by Django 4.1 on 2022-08-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(verbose_name='Facebook url')),
                ('twitter', models.URLField(verbose_name='Twitter url')),
                ('linkedin', models.URLField(verbose_name='Linkedin url')),
                ('youtube', models.URLField(verbose_name='Youtube url')),
                ('be', models.URLField(verbose_name='Be url')),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
            },
        ),
    ]
