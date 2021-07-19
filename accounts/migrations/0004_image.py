# Generated by Django 3.0.5 on 2021-07-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210719_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
