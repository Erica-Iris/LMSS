# Generated by Django 3.2.9 on 2021-11-11 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_receipt', models.CharField(max_length=100, verbose_name='发票号')),
                ('get_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': '发票',
                'verbose_name_plural': '发票',
                'db_table': '',
                'managed': True,
            },
        ),
    ]