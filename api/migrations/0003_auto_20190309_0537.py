# Generated by Django 2.1.7 on 2019-03-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190309_0504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daily',
            options={'ordering': ('-completed', 'title')},
        ),
        migrations.AddField(
            model_name='daily',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
