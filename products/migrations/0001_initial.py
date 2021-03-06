# Generated by Django 2.0.5 on 2018-06-04 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skq', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('serial', models.CharField(max_length=250)),
                ('quantity', models.FloatField()),
                ('unit_cost', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('rack_location', models.FloatField()),
                ('notes', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('status', models.IntegerField(verbose_name=1)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductBrand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='purchases',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductPurchase'),
        ),
    ]
