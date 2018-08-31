from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, \
        FieldRowPanel, MultiFieldPanel, InlinePanel, PageChooserPanel


class GoogleMapBlock(blocks.StructBlock):
    map_long = blocks.CharBlock(required=True,max_length=255)
    map_lat = blocks.CharBlock(required=True,max_length=255)
    map_zoom_level = blocks.CharBlock(default=14,required=True,max_length=3)

    class Meta:
        template = 'blocks/google_map.html'
        icon = 'cogs'
        label = 'Google Map'

class TwoColumnBlock(blocks.StructBlock):

    # background = blocks.ChoiceBlock(choices=COLOUR_CHOICES,default="white")
    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
        ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
        ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'yourapp/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'
