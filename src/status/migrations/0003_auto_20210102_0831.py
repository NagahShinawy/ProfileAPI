# Generated by Django 3.1.4 on 2021-01-02 06:31

from django.db import migrations, models
import status.models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20210102_0814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ('-pk',), 'verbose_name': 'Status Post', 'verbose_name_plural': 'Status Posts'},
        ),
        migrations.AlterField(
            model_name='status',
            name='date',
            field=models.DateField(blank=True, null=True, validators=[status.models.no_future, status.models.no_past]),
        ),
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=status.models.upload_status_img),
        ),
    ]
