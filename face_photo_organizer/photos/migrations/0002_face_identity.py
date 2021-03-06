# Generated by Django 3.2.8 on 2022-03-18 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Face',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.identity')),
            ],
        ),
    ]
