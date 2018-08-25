# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 03:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0104_add_skip_during_manual_grading_permission_to_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticationToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation time')),
                ('last_use_time', models.DateTimeField(blank=True, null=True, verbose_name='Last use time')),
                ('valid_until', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Valid until')),
                ('revocation_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Revocation time')),
                ('token_hash', models.CharField(blank=True, help_text='A hash of the authentication token to be used for direct git access.', max_length=200, null=True, unique=True, verbose_name='Hash of git authentication token')),
                ('participation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Participation', verbose_name='Participation')),
                ('restrict_to_participation_role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.ParticipationRole', verbose_name='Restrict to role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
        ),
    ]
