# Generated by Django 5.0 on 2023-12-23 12:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurancemanagement', '0004_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=150)),
                ('policy_desc', models.TextField()),
                ('sum_insurance', models.BigIntegerField()),
                ('premium', models.BigIntegerField()),
                ('tenure', models.BigIntegerField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurancemanagement.category')),
            ],
        ),
    ]
