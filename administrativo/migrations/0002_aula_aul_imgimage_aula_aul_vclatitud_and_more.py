# Generated by Django 4.2.7 on 2023-11-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='aul_imgImage',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='aulas'),
        ),
        migrations.AddField(
            model_name='aula',
            name='aul_vcLatitud',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='aula',
            name='aul_vcLongitud',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Longitud'),
        ),
    ]
