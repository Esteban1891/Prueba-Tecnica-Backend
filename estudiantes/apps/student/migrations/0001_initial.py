# Generated by Django 3.1.6 on 2021-06-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('complete_name', models.CharField(max_length=150)),
                ('document', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], max_length=50)),
                ('note', models.IntegerField()),
                ('autoevaluation', models.IntegerField()),
            ],
        ),
    ]