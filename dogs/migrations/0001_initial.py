# Generated by Django 4.0.2 on 2022-03-05 03:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('size', models.CharField(choices=[('T', 'Tiny'), ('s', 'Small'), ('m', 'Medium'), ('l', 'Large')], default='s', max_length=6)),
                ('friendliness', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('trainability', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('sheddingamount', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('exerciseneeds', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('favoritefood', models.CharField(max_length=200)),
                ('favoritetoy', models.CharField(max_length=200)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breed', to='dogs.breed')),
            ],
        ),
    ]
