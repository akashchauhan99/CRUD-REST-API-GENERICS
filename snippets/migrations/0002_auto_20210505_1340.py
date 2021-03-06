# Generated by Django 3.2.1 on 2021-05-05 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogText', models.CharField(max_length=500)),
                ('blogImg', models.FileField(upload_to='')),
                ('pubDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=120)),
                ('lastName', models.CharField(max_length=120)),
                ('userName', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
        migrations.AddField(
            model_name='blog',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.user'),
        ),
    ]
