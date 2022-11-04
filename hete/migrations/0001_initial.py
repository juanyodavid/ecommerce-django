# Generated by Django 3.2.12 on 2022-04-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('observation', models.CharField(max_length=255)),
                ('cellphone', models.CharField(max_length=16)),
                ('location', models.URLField()),
                ('house_photo', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Dispatcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('cellphone', models.IntegerField()),
                ('debt', models.DecimalField(decimal_places=3, max_digits=6)),
                ('zone', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Food_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('description', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=63)),
                ('name2', models.CharField(max_length=63)),
                ('ruc1', models.CharField(max_length=63)),
                ('ruc2', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('state', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='hete.Food_category')),
            ],
        ),
    ]
