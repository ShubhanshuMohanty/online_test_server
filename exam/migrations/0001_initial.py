# Generated by Django 5.2 on 2025-05-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='McqQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
                ('answer', models.CharField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3'), ('option4', 'Option 4')], max_length=10)),
            ],
        ),
    ]
