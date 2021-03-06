# Generated by Django 3.1.7 on 2021-02-21 04:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('address', models.CharField(max_length=75)),
                ('availability', models.CharField(choices=[('O', 'Open'), ('P', 'Partial'), ('C', 'Closed')], max_length=1)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['-date_updated'],
            },
        ),
    ]
