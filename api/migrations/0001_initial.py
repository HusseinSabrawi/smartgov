# Generated by Django 3.1.7 on 2021-04-11 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=15, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=511)),
                ('last_name', models.CharField(max_length=511)),
                ('email', models.CharField(max_length=511)),
                ('role', models.CharField(max_length=511)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizen_id', models.CharField(max_length=15, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=511)),
                ('last_name', models.CharField(max_length=511)),
                ('email', models.CharField(max_length=511)),
                ('address', models.CharField(max_length=16000)),
                ('birthdate', models.DateField()),
                ('authenticated', models.BooleanField(default=False)),
                ('profile_pic', models.URLField(blank=True, max_length=16000)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=2047)),
                ('picture', models.URLField(blank=True, max_length=16000)),
                ('details', models.CharField(blank=True, max_length=16000)),
                ('status', models.CharField(default='Just Arrived', max_length=2047)),
                ('is_completed', models.BooleanField(default=False)),
                ('date_arrived', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('private', models.BooleanField(default=False)),
                ('citizen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.citizen', to_field='citizen_id')),
                ('current_agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agent', to_field='employee_id')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.URLField(blank=True, max_length=16000)),
                ('text', models.CharField(blank=True, max_length=16000)),
                ('category', models.CharField(max_length=2047)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=2047)),
                ('picture', models.URLField(blank=True, max_length=16000)),
                ('details', models.CharField(blank=True, max_length=16000)),
                ('status', models.CharField(default='Just Arrived', max_length=2047)),
                ('is_completed', models.BooleanField(default=False)),
                ('date_arrived', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('citizen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.citizen', to_field='citizen_id')),
                ('current_agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agent', to_field='employee_id')),
            ],
        ),
        migrations.CreateModel(
            name='RequestTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_on_arrival', models.CharField(max_length=255)),
                ('status_on_departure', models.CharField(blank=True, max_length=255)),
                ('date_arrived', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agent', to_field='employee_id')),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.request')),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_on_arrival', models.CharField(max_length=255)),
                ('status_on_departure', models.CharField(blank=True, max_length=255)),
                ('date_arrived', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agent', to_field='employee_id')),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.complaint')),
            ],
        ),
    ]
