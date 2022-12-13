# Generated by Django 4.1.4 on 2022-12-13 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_alter_users_first_name_alter_users_last_name_words'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('url', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='words.users')),
            ],
        ),
    ]
