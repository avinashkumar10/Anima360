# Generated by Django 3.0.5 on 2021-07-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210719_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterShelterScreen4Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_details', models.CharField(default='', max_length=200)),
                ('purchase_date', models.DateField(blank=True, verbose_name='Purchase Date (mm/dd/yyyy)')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('product_quantity', models.IntegerField()),
                ('amount', models.FloatField()),
                ('upload_bill', models.ImageField(upload_to='images')),
            ],
        ),
    ]
