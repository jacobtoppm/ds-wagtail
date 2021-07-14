# Generated by Django 3.1.8 on 2021-07-09 14:22

from django.db import migrations
import etna.collections.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0007_add_alerts'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicexplorerpage',
            name='body',
            field=wagtail.core.fields.StreamField([('collection_highlights', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Collection Highlights', max_length=100))])), ('featured_page', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('page', wagtail.core.blocks.PageChooserBlock())])), ('promoted_pages', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('sub_heading', wagtail.core.blocks.CharBlock(max_length=200)), ('promoted_items', wagtail.core.blocks.ListBlock(etna.collections.blocks.PromotedItemBlock, max=3, min=3))]))], blank=True),
        ),
    ]
