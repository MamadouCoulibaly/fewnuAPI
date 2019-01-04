# Generated by Django 2.1.4 on 2019-01-04 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=30)),
                ('prix', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriquePrets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Prets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomclient', models.CharField(max_length=30)),
                ('libelle', models.CharField(max_length=30)),
                ('montant', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('nom', models.CharField(max_length=30)),
                ('numero', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ventes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=30)),
                ('prix', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIREST.Users')),
            ],
        ),
        migrations.AddField(
            model_name='prets',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIREST.Users'),
        ),
        migrations.AddField(
            model_name='historiqueprets',
            name='prets_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIREST.Prets'),
        ),
        migrations.AddField(
            model_name='depenses',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIREST.Users'),
        ),
    ]