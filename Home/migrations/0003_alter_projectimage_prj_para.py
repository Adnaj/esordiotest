# Generated by Django 4.2.3 on 2023-07-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_projectimage_delete_projectimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='prj_para',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
