# Generated by Django 5.0.2 on 2024-03-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_data_project_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='prj_client_machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
            ],
        ),
    ]
