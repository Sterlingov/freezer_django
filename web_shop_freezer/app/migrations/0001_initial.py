# Generated by Django 4.0.6 on 2022-07-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('char_freeze', models.IntegerField()),
                ('char_ozu', models.IntegerField()),
                ('char_weight', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
