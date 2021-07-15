from wagtail.core import blocks

from ..quotes.blocks import QuoteBlock
from ..paragraphs.blocks import ParagraphWithHeading
from ..media_embeds.blocks import MediaEmbedAudioBlock, MediaEmbedVideoBlock
from ..sections.blocks import SectionHeadingBlock

class InsightsPageStreamBlock(blocks.StreamBlock):
    quote = QuoteBlock()
    paragraph_with_heading = ParagraphWithHeading()
    media_embed_audio = MediaEmbedAudioBlock()
    media_embed_video = MediaEmbedVideoBlock()
    section_heading = SectionHeadingBlock()
