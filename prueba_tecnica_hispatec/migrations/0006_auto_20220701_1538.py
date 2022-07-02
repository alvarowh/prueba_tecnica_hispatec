# Generated by Django 3.0 on 2022-07-01 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prueba_tecnica_hispatec', '0005_auto_20220701_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_lending',
            name='lend_expected_finish_date',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_lending',
            name='lend_real_finish_date',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_lending',
            name='lend_start_date',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=False,
        ),
    ]