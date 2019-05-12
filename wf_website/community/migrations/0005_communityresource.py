# Generated by Django 2.1.7 on 2019-05-12 12:48

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('community', '0004_communitypage_intro_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityResource',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('resource_type', models.CharField(choices=[('online_worship', 'Online Worship'), ('community_directory', 'Community Directory')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
