# Generated by Django 2.0 on 2020-04-07 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_chef', '0005_auto_20200407_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clases',
            name='pagado',
        ),
        migrations.AddField(
            model_name='clases',
            name='gratis',
            field=models.BooleanField(db_column='Pagado', default=False),
        ),
        migrations.AlterField(
            model_name='clases',
            name='descripcion',
            field=models.TextField(db_column='Descripcion'),
        ),
        migrations.AlterField(
            model_name='clases',
            name='ingredientes',
            field=models.TextField(db_column='Ingredientes'),
        ),
    ]
