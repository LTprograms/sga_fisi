# Generated by Django 4.2.7 on 2023-11-12 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0001_initial'),
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('aul_iCodigo', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('aul_vcCodigo', models.CharField(max_length=16, verbose_name='Código')),
                ('aul_iCapacidad', models.IntegerField(verbose_name='Capacidad')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
                'db_table': 'aula',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('loc_iCodigo', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('loc_vcCodigo', models.CharField(max_length=32, verbose_name='Código')),
                ('loc_vcNombre', models.CharField(max_length=64, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
                'db_table': 'local',
            },
        ),
        migrations.CreateModel(
            name='GrupoHorario',
            fields=[
                ('gruhor_iCodigo', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('gruhor_tHoraInicio', models.TimeField(verbose_name='Hora de inicio')),
                ('gruhor_tHoraFinal', models.TimeField(verbose_name='Hora de finalización')),
                ('aul_iCodigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.aula', verbose_name='Aula')),
                ('curtip_iCodigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.cursotipodictado', verbose_name='Tipo de dictado')),
                ('dia_iCodigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.dia', verbose_name='Día')),
                ('gru_iCodigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.grupo', verbose_name='Grupo')),
            ],
            options={
                'verbose_name': 'Grupo horario',
                'verbose_name_plural': 'Grupos horario',
                'db_table': 'grupo_horario',
            },
        ),
        migrations.AddField(
            model_name='aula',
            name='loc_iCodigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.local', verbose_name='Local'),
        ),
    ]
