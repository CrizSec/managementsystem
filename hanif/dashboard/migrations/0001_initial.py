# Generated by Django 5.0.3 on 2024-03-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item_name', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True, null=True)),
                ('stock', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
