# Generated by Django 3.2.5 on 2021-10-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_notasaulas'),
    ]

    operations = [
        migrations.AddField(
            model_name='aulas',
            name='capa',
            field=models.ImageField(default=1, upload_to='capa'),
            preserve_default=False,
        ),
    ]
