# Generated by Django 5.0.6 on 2025-06-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tampilanutama_app', '0010_alter_organizationmember_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationmember',
            name='division',
            field=models.CharField(choices=[('None', 'None (Untuk Ketua/Sekum/Bendahara Umum)'), ('Kader', 'Kader'), ('Riset & Pengembangan Keilmuan', 'Riset & Pengembangan Keilmuan'), ('Media & Komunikasi', 'Media & Komunikasi'), ('Organisasi', 'Organisasi'), ('Hikmah, Politik, & Kebijakan Publik', 'Hikmah, Politik, dan Kebijakan Publik')], default='None', max_length=100, verbose_name='Bidang/Divisi'),
        ),
    ]
