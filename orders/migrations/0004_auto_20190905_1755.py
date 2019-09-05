# Generated by Django 2.2.4 on 2019-09-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_address_locality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_country',
            field=models.CharField(default='United States', help_text='Country for shipping.', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_locality',
            field=models.CharField(help_text='City for the shipping address.', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_region',
            field=models.CharField(help_text='State for the shipping address.', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(help_text='Provide an email, so we can communicate any issues regarding this order.', max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='family_name',
            field=models.CharField(blank=True, default='', help_text='Enter the family name for the recipient.', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='given_name',
            field=models.CharField(default='', help_text='Enter the given name for the recipient.', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='po_box_number',
            field=models.CharField(blank=True, default='', help_text='P.O. Box, if relevant.', max_length=32),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(help_text='Postal code for the shipping address.', max_length=16),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address',
            field=models.CharField(blank=True, default='', help_text='The street address where this order should be shipped.', max_length=255),
        ),
    ]
