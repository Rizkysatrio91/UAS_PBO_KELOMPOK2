# Generated by Django 5.0.6 on 2025-06-14 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tampilanutama_app', '0002_siteconfiguration_site_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopBarConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nomor Telepon')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Alamat Email')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alamat Singkat')),
                ('facebook_url', models.URLField(blank=True, null=True, verbose_name='URL Facebook')),
                ('twitter_url', models.URLField(blank=True, null=True, verbose_name='URL Twitter')),
                ('instagram_url', models.URLField(blank=True, null=True, verbose_name='URL Instagram')),
                ('youtube_url', models.URLField(blank=True, null=True, verbose_name='URL YouTube')),
            ],
            options={
                'verbose_name': 'Konfigurasi Top Bar',
                'verbose_name_plural': 'Konfigurasi Top Bar',
            },
        ),
    ]
