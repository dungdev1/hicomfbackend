# Generated by Django 3.1.2 on 2020-10-16 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0011_auto_20201016_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='mains.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='ending_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='starting_year',
            field=models.IntegerField(null=True),
        ),
    ]