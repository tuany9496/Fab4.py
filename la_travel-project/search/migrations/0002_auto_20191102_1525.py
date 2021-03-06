# Generated by Django 2.2.6 on 2019-11-02 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='CuisineCodeDescription',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='place',
            name='Faceobok',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='place',
            name='FridayClose',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='FridayOpen',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='SICCode',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='place',
            name='SICDescription',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='place',
            name='SaturdayClose',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='SaturdayOpen',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='SundayClose',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='SundayOpen',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='ThursdayClose',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='ThursdayOpen',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='TuesdayClose',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='TuesdayOpen',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='Twitter',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='place',
            name='WednesdayClose',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='WednesdayOpen',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='place',
            name='addressName',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='cityName',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='companyName',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='countyName',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='neigbhorhoodName',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='stateName',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='websiteLink',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='zipName',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
