# Generated by Django 3.1.8 on 2021-07-22 15:13

from django.db import migrations
import etna.records.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0006_record_embed_blocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insightspage',
            name='body',
            field=wagtail.core.fields.StreamField([('quote', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('quote', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], required=True)), ('attribution', wagtail.core.blocks.CharBlock(max_length=100, required=False))])), ('paragraph_with_heading', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], required=True))])), ('promoted_item', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Title of the promoted page', max_length=100)), ('category', wagtail.snippets.blocks.SnippetChooserBlock('categories.Category')), ('publication_date', wagtail.core.blocks.DateBlock()), ('url', wagtail.core.blocks.URLBlock(help_text='URL for the external page', label='external URL')), ('cta_label', wagtail.core.blocks.CharBlock(help_text='The button label', label='CTA label', max_length=50)), ('teaser_image', wagtail.images.blocks.ImageChooserBlock(help_text='An image used to create a teaser for the promoted page')), ('teaser_alt_text', wagtail.core.blocks.CharBlock(help_text='Alt text of the teaser image', max_length=100)), ('description', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='A description of the promoted page'))])), ('featured_record', wagtail.core.blocks.StructBlock([('record', etna.records.blocks.RecordChooserBlock())])), ('featured_records', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('introduction', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('records', wagtail.core.blocks.ListBlock(etna.records.blocks.RecordChooserBlock))]))], blank=True, null=True),
        ),
    ]
