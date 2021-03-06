# Generated by Django 2.2.12 on 2021-05-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='默认用户', max_length=28)),
                ('count', models.CharField(max_length=128, unique=True)),
                ('sex', models.CharField(default='男', max_length=10)),
                ('age', models.IntegerField(default=18)),
                ('universiy', models.CharField(default='世界一流大学', max_length=64)),
            ],
            options={
                'verbose_name': '用户',
                'db_table': '用户',
            },
        ),
    ]
