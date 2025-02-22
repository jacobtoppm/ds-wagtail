from django.utils.functional import cached_property
from wagtail.core import blocks


class SectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        required=True,
        max_length=100,
        label="Section heading (heading level 2)"
    )

    class Meta:
        icon = "fa-header"
        label = "Section heading"
        template = "sections/blocks/section.html"
