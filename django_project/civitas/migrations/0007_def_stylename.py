# Generated by Django 2.2.15 on 2023-07-27 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('civitas', '0005_vector_tile_geom_type'),
    ]

    sql = """
        ALTER TABLE asset_classification_combination ADD COLUMN def_stylename TEXT;
    """

    operations = [
        migrations.RunSQL(sql)
    ]
