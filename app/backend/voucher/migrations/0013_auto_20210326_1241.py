# Generated by Django 3.1 on 2021-03-26 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20210326_1214'),
        ('voucher', '0012_auto_20210326_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voucher_to_organization', to='organization.organization'),
        ),
    ]