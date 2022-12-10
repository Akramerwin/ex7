# Generated by Django 4.1.2 on 2022-12-10 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.TextField(verbose_name='question'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_date', models.DateTimeField(auto_now_add=True, verbose_name='a_date')),
                ('Choice_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_a', to='webapp.choice', verbose_name='choice_a')),
                ('Poll_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll_a', to='webapp.poll', verbose_name='poll_a')),
            ],
        ),
    ]
