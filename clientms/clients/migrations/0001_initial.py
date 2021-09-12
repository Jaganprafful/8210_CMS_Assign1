# Generated by Django 2.2 on 2021-09-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50)),
                ('address', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('city', models.CharField(default=' ', max_length=50)),
                ('state', models.CharField(default='NE', max_length=50)),
                ('zipcode', models.CharField(default='00000', max_length=10)),
                ('email', models.EmailField(default=' ', max_length=100)),
                ('cell_phone', models.CharField(default='(402)000-0000', max_length=50)),
                ('acct_number', models.CharField(blank=True, default='00000', max_length=50, null=True)),
                ('notes', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
            ],
        ),
    ]
