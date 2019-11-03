# Generated by Django 2.2.6 on 2019-11-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200)),
                ('cityName', models.CharField(max_length=200)),
                ('stateName', models.CharField(max_length=200)),
                ('zipName', models.CharField(max_length=200)),
                ('countyName', models.CharField(max_length=200)),
                ('neigbhorhoodName', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=200)),
                ('websiteLink', models.CharField(max_length=200)),
                ('addressName', models.CharField(max_length=200)),
            ],
        ),
    ]
