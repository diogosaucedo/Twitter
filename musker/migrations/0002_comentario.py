# Generated by Django 5.0 on 2023-12-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('data_postagem', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
