# Generated by Django 5.0.6 on 2024-06-05 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
