# Generated by Django 3.2.6 on 2021-10-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_wein_alk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Braende',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artikelnr', models.IntegerField()),
                ('titel', models.CharField(max_length=100)),
                ('land', models.CharField(choices=[('Deutschland', 'DE'), ('Oesterreich', 'AT')], max_length=20)),
                ('region', models.CharField(choices=[('Region1', '1'), ('Region2', '2'), ('Region3', '3'), ('Region4', '4')], max_length=30)),
                ('jahrgang', models.IntegerField(default=2020)),
                ('inhalt', models.DecimalField(decimal_places=2, default=0.75, max_digits=3)),
                ('alk', models.DecimalField(decimal_places=1, default=10.0, max_digits=3)),
                ('added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Likoere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artikelnr', models.IntegerField()),
                ('titel', models.CharField(max_length=100)),
                ('land', models.CharField(choices=[('Deutschland', 'DE'), ('Oesterreich', 'AT')], max_length=20)),
                ('region', models.CharField(choices=[('Region1', '1'), ('Region2', '2'), ('Region3', '3'), ('Region4', '4')], max_length=30)),
                ('jahrgang', models.IntegerField(default=2020)),
                ('inhalt', models.DecimalField(decimal_places=2, default=0.75, max_digits=3)),
                ('alk', models.DecimalField(decimal_places=1, default=10.0, max_digits=3)),
                ('added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sonstiges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artikelnr', models.IntegerField()),
                ('titel', models.CharField(max_length=100)),
                ('land', models.CharField(choices=[('Deutschland', 'DE'), ('Oesterreich', 'AT')], max_length=20)),
                ('region', models.CharField(choices=[('Region1', '1'), ('Region2', '2'), ('Region3', '3'), ('Region4', '4')], max_length=30)),
                ('jahrgang', models.IntegerField(default=2020)),
                ('inhalt', models.DecimalField(decimal_places=2, default=0.75, max_digits=3)),
                ('alk', models.DecimalField(decimal_places=1, default=10.0, max_digits=3)),
                ('added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spirituosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artikelnr', models.IntegerField()),
                ('titel', models.CharField(max_length=100)),
                ('land', models.CharField(choices=[('Deutschland', 'DE'), ('Oesterreich', 'AT')], max_length=20)),
                ('region', models.CharField(choices=[('Region1', '1'), ('Region2', '2'), ('Region3', '3'), ('Region4', '4')], max_length=30)),
                ('jahrgang', models.IntegerField(default=2020)),
                ('inhalt', models.DecimalField(decimal_places=2, default=0.75, max_digits=3)),
                ('alk', models.DecimalField(decimal_places=1, default=10.0, max_digits=3)),
                ('added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='wein',
            name='alk',
            field=models.DecimalField(decimal_places=1, default=10.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='wein',
            name='inhalt',
            field=models.DecimalField(decimal_places=2, default=0.75, max_digits=3),
        ),
        migrations.AlterField(
            model_name='wein',
            name='jahrgang',
            field=models.IntegerField(default=2020),
        ),
    ]
