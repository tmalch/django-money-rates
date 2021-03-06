# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 11:13
from __future__ import unicode_literals

from django.db import migrations
from djmoney_rates.settings import money_rates_settings

def load_default_rates(apps, schema_editor):
   
   backend_class = money_rates_settings.DEFAULT_BACKEND
   backend = backend_class()
   
   RateSource = apps.get_model("djmoney_rates", "RateSource")
   source = RateSource.objects.create(name=backend.get_source_name(), base_currency=backend.get_base_currency())   
   
   Rates = apps.get_model("djmoney_rates", "Rate")
   Rates.objects.create(currency=source.base_currency, value=1, source=source)

class Migration(migrations.Migration):

    dependencies = [
        ('djmoney_rates', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_default_rates),
    ]

