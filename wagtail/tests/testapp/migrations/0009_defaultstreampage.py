# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 11:37
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0029_unicode_slugfield_dj19"),
        ("tests", "0008_inlinestreampage_inlinestreampagesection"),
    ]

    operations = [
        migrations.CreateModel(
            name="DefaultStreamPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        (
                            ("text", wagtail.core.blocks.CharBlock()),
                            ("rich_text", wagtail.core.blocks.RichTextBlock()),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                        ),
                        default="",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
