# Generated by Django 2.0.7 on 2019-03-19 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viewflow', '0006_i18n'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.Process')),
                ('planet', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('approved_at', models.DateTimeField(null=True)),
                ('drop_status', models.CharField(choices=[('SCF', 'Successful'), ('ERR', 'Unsuccessful')], default=None, max_length=3, null=True)),
                ('delivery_report', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
