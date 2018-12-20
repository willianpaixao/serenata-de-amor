# Generated by Django 2.0.8 on 2018-09-13 05:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamber_of_deputies', '0006_change_on_delete_social_media_to_set_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reimbursement',
            name='document_id',
            field=models.IntegerField(db_index=True, verbose_name='Número do Reembolso'),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='issue_date',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='Data de Emissão'),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128, verbose_name='Números dos Ressarcimentos'), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='supplier',
            field=models.CharField(max_length=256, verbose_name='Fornecedor'),
        ),
    ]
