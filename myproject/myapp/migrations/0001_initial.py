# Generated by Django 4.2.5 on 2024-02-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cousine', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
