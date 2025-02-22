# Generated by Django 3.1.8 on 2021-10-13 16:11

from django.db import migrations
import etna.home.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_richtext_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('featured_items', etna.home.blocks.FeaturedItemsBlock()), ('paragraph_with_heading', wagtail.core.blocks.StructBlock([('heading_level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'Heading level 2'), ('h3', 'Heading level 3'), ('h4', 'Heading level 4')], help_text='Use this field to select the appropriate heading tag. Check where this component will sit in the page to ensure that it follows the correct heading order and avoids skipping levels e.g. an &lt;h4&gt; should not follow an &lt;h2&gt;. For further information, see: <a href=https://www.w3.org/WAI/tutorials/page-structure/headings target=_blank>https://www.w3.org/WAI/tutorials/page-structure/headings/<a>')), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ul'], required=True))]))], blank=True, null=True),
        ),
    ]
