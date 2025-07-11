# Generated by Django 5.2.1 on 2025-06-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('code', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='food_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
