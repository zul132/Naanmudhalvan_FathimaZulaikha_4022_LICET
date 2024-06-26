# Generated by Django 5.0.4 on 2024-04-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('categorie', models.CharField(default=None, max_length=100, null=True)),
                ('artist', models.CharField(max_length=100)),
                ('audio_file', models.FileField(upload_to='audio/')),
                ('audio_img', models.FileField(upload_to='audio_img/')),
            ],
        ),
    ]
