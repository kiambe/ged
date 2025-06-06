# Generated by Django 5.2 on 2025-05-10 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landscape', '0004_alter_projectorganism_technology'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_duration',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.AddField(
            model_name='project',
            name='end_year',
            field=models.IntegerField(blank=True, default=1900, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='start_year',
            field=models.IntegerField(blank=True, default=1990, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('Not started)', 'Not started'), ('Started', 'Started'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='nature_of_partnership',
            field=models.CharField(blank=True, choices=[('Public-Private Partnership (PPP)', 'Public-Private Partnership (PPP)'), ('Public-Public Partnership (PuP)', 'Public-Public Partnership (PuP)'), ('Private-Private Partnership (PrP)', 'Private-Private Partnership (PrP)'), ('Public-Academic Partnership', 'Public-Academic Partnership'), ('Private-Academic Partnership', 'Private-Academic Partnership'), ('Public-Civil Society Partnership', 'Public-Civil Society Partnership'), ('Multistakeholder Partnerships (MSP)', 'Multistakeholder Partnerships (MSP)'), ('Donor-Government Partnership', 'Donor-Government Partnership'), ('Public-Development Finance Institution (DFI) Partnership', 'Public-Development Finance Institution (DFI) Partnership'), ('Research-Industry Partnership', 'Research-Industry Partnership'), ('Intergovernmental Partnerships', 'Intergovernmental Partnerships'), ('Public-International Organization Partnership', 'Public-International Organization Partnership')], max_length=100, null=True),
        ),
    ]
