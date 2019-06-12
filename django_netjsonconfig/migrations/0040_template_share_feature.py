# Generated by Django 2.1.9 on 2019-06-07 18:32

import django.core.validators
from django.db import migrations, models
import django_netjsonconfig.utils
import jsonfield.fields
import re


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0039_vpn_format_dh'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='default_values',
            field=jsonfield.fields.JSONField(blank=True, default=dict, help_text='A dictionary containing the default values for the variables used by this template; these default variables will be used during schema validation.', verbose_name='Default Values'),
        ),
        migrations.AddField(
            model_name='template',
            name='description',
            field=models.TextField(blank=True, help_text='Public description of this template', null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='template',
            name='key',
            field=models.CharField(blank=True, default=django_netjsonconfig.utils.get_random_key, help_text='Secret key needed to import the template', max_length=64, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[^\\s/\\.]+$'), code='invalid', message='Key must not contain spaces, dots or slashes.')], verbose_name='Secret key'),
        ),
        migrations.AddField(
            model_name='template',
            name='notes',
            field=models.TextField(blank=True, help_text='Internal notes for administrators', null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='template',
            name='sharing',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('secret_key', 'Shared via secret key'), ('import', 'Import')], db_index=True, default='private', help_text='Whether to keep this template private, share it publicly, share it privately using a secret key or import its contents from another source', max_length=16, verbose_name='Sharing settings'),
        ),
        migrations.AddField(
            model_name='template',
            name='url',
            field=models.URLField(blank=True, help_text='URL from which the template will be imported', null=True, verbose_name='Import URL'),
        ),
    ]
