# Generated by Django 3.0.5 on 2021-02-19 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbloptions',
            fields=[
                ('optionid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='')),
                ('email', models.TextField(blank=True, null=True)),
                ('mobile', models.TextField(blank=True, null=True)),
                ('alternate_phone', models.TextField(blank=True, null=True)),
                ('facebook_link', models.TextField(blank=True, null=True)),
                ('twitter_link', models.TextField(blank=True, null=True)),
                ('instagram_link', models.TextField(blank=True, null=True)),
                ('linkedin_link', models.TextField(blank=True, null=True)),
                ('github_link', models.TextField(blank=True, null=True)),
                ('google_var_id', models.TextField(blank=True, null=True)),
                ('google_ana_script', models.TextField(blank=True, null=True)),
                ('facebook_script', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('meta_title', models.TextField(blank=True, null=True)),
                ('meta_keywords', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('createdon', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tblsubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=150, null=True)),
                ('price', models.CharField(blank=True, max_length=150, null=True)),
                ('validity', models.IntegerField(blank=True, null=True)),
                ('isactive', models.IntegerField(blank=True, default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userpdfs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.TextField(blank=True, null=True)),
                ('filesize', models.TextField(blank=True, null=True)),
                ('files', models.FileField(null=True, upload_to='documents/')),
                ('createdon', models.DateTimeField(auto_now=True, null=True)),
                ('userid', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tbluserdetails',
            fields=[
                ('detailid', models.AutoField(primary_key=True, serialize=False)),
                ('purchasedate', models.DateTimeField(blank=True, null=True)),
                ('expiredate', models.DateTimeField(blank=True, null=True)),
                ('orderid', models.TextField(blank=True, null=True)),
                ('paymentid', models.TextField(blank=True, null=True)),
                ('subscription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Tblsubscription')),
                ('userid', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tblcommonmasters',
            fields=[
                ('autoid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('isactive', models.IntegerField(blank=True, default=1, null=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='')),
                ('type', models.TextField(blank=True, null=True)),
                ('createdon', models.DateTimeField(blank=True, null=True)),
                ('otherfield', models.CharField(blank=True, max_length=350, null=True)),
                ('userid', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
