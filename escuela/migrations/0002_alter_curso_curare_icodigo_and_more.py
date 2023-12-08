# Generated by Django 4.2.7 on 2023-11-13 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_alter_escuela_areaca_icodigo'),
        ('vicerrectorado', '0001_initial'),
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curare_iCodigo',
            field=models.ForeignKey(limit_choices_to={'areaca_bActivo': 1}, on_delete=django.db.models.deletion.CASCADE, to='general.areaacademica', verbose_name='Área académica'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='curtip_iCodigo',
            field=models.ForeignKey(limit_choices_to={'curtip_bActivo': 1}, on_delete=django.db.models.deletion.CASCADE, to='escuela.cursotipo', verbose_name='Tipo de acceso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='plaest_iCodigo',
            field=models.ForeignKey(limit_choices_to={'plaest_bActivo': 1}, on_delete=django.db.models.deletion.CASCADE, to='escuela.planestudio', verbose_name='Plan de estudio'),
        ),
        migrations.AlterField(
            model_name='cursohorasdictado',
            name='curtip_iCodigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.cursotipodictado', verbose_name='Tipo de dictado del curso'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='sem_iCodigo',
            field=models.ForeignKey(limit_choices_to={'sem_cActivo': 'S'}, on_delete=django.db.models.deletion.CASCADE, to='vicerrectorado.semestre', verbose_name='Semestre'),
        ),
        migrations.AlterField(
            model_name='planestudio',
            name='esc_iCodigo',
            field=models.ForeignKey(limit_choices_to={'esc_bActivo': 1}, on_delete=django.db.models.deletion.CASCADE, to='general.escuela', verbose_name='Escuela'),
        ),
    ]
