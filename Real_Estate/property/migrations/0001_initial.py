# Generated by Django 3.0.5 on 2020-08-07 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Type of Building',
                'verbose_name_plural': 'Types of Building',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(verbose_name='Property Price')),
                ('description', models.TextField(verbose_name='Property Details')),
                ('location', models.CharField(max_length=200, verbose_name='Property Location')),
                ('date_added', models.DateField(default=django.utils.timezone.now, verbose_name='Date Registered')),
                ('bedrooms', models.IntegerField(default=0, verbose_name='Number of Bedrooms')),
                ('kitchens', models.IntegerField(default=0, verbose_name='Number of Kitchens')),
                ('living_rooms', models.IntegerField(default=0, verbose_name='Number of Living Rooms')),
                ('parking', models.IntegerField(default=0, verbose_name='Number of Parking Lots')),
                ('picture_1', models.ImageField(upload_to='media/property')),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='media/property')),
                ('picture_3', models.ImageField(blank=True, null=True, upload_to='media/property')),
                ('picture_4', models.ImageField(blank=True, null=True, upload_to='media/property')),
                ('availability', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Agent.Agent', verbose_name='Agent')),
                ('building_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.BuildingType', verbose_name='Property Type')),
            ],
            options={
                'verbose_name_plural': 'Properties',
                'ordering': ['name', 'price'],
            },
        ),
        migrations.CreateModel(
            name='SaleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Type of Sale',
                'verbose_name_plural': 'Types of Sale',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PropertyEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(verbose_name='Customer Message')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Property', verbose_name='Property Details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'Property Inquiry',
                'verbose_name_plural': 'Property Inquiries',
                'ordering': ['date', 'property'],
            },
        ),
        migrations.AddField(
            model_name='property',
            name='sale_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.SaleType', verbose_name='Type of Sale'),
        ),
    ]
