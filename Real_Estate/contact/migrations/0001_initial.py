# Generated by Django 3.0.5 on 2020-08-07 07:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Question Tag',
                'verbose_name_plural': 'Question Tags',
                'ordering': ('name', 'description'),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('tags', models.ManyToManyField(related_name='Tags', to='contact.QuestionTag')),
            ],
            options={
                'verbose_name': 'Contact Question',
                'verbose_name_plural': 'Contact Questions',
                'ordering': ('name', 'subject'),
            },
        ),
    ]
