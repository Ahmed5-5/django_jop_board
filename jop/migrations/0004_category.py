# Generated by Django 4.1.7 on 2023-03-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0003_jop_description_jop_experience_jop_jop_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
