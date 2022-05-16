# Generated by Django 4.0.4 on 2022-05-16 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EXAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('about', models.TextField()),
                ('conducted_by', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OPTION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QUESTION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic.exam')),
            ],
        ),
        migrations.CreateModel(
            name='RESPONSE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentRollNumber', models.CharField(max_length=20)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic.exam')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic.question')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic.option')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic.question'),
        ),
        migrations.CreateModel(
            name='ANSWER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic.question')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic.option')),
            ],
        ),
    ]
