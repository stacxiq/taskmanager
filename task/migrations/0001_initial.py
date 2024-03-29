# Generated by Django 3.2 on 2021-05-08 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_description', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='start_date')),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('status', models.CharField(choices=[('1', 'staging'), ('2', 'in progress'), ('3', 'test'), ('4', 'in review'), ('5', 'closed')], max_length=265)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.employee')),
            ],
        ),
    ]
