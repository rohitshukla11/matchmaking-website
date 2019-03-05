# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('my_answer_importance', models.CharField(max_length=50, choices=[('Mandatory', 'Mandatory'), ('Very Important', 'Very Important'), ('Somewhat Important', 'Somewhat Important'), ('Not Important', 'Not Important')])),
                ('their_importance', models.CharField(max_length=50, choices=[('Mandatory', 'Mandatory'), ('Very Important', 'Very Important'), ('Somewhat Important', 'Somewhat Important'), ('Not Important', 'Not Important')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(related_name='user_answer', to='questions.Answer')),
                ('question', models.ForeignKey(to='questions.Question')),
                ('their_answer', models.ForeignKey(blank=True, null=True, related_name='match_answer', to='questions.Answer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
