# Generated by Django 3.1.2 on 2020-10-05 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mains', '0005_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='privacy',
            field=models.CharField(choices=[('P', 'Public'), ('F', 'Friends'), ('O', 'Only me')], default='P', max_length=2),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('starting_year', models.IntegerField()),
                ('ending_year', models.IntegerField(blank=True, null=True)),
                ('graduated', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('concentration', models.CharField(max_length=100)),
                ('degree', models.CharField(blank=True, max_length=150)),
                ('privacy', models.CharField(choices=[('P', 'Public'), ('F', 'Friends'), ('O', 'Only me')], default='P', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
