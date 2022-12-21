# Generated by Django 4.1.4 on 2022-12-21 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Dictionaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Dictionary',
                'verbose_name_plural': 'Dictionaries',
            },
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200, unique=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_clear', models.DateTimeField(blank=True, null=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='words.categories')),
            ],
            options={
                'verbose_name': 'Word',
                'verbose_name_plural': 'Words',
            },
        ),
    ]
