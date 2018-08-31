from .blocks import *

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, \
        FieldRowPanel, MultiFieldPanel, InlinePanel, PageChooserPanel


class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", null=True, blank=True)),
        ('paragraph', blocks.RichTextBlock(null=True, blank=True)),
        ('image', ImageChooserBlock(null=True, blank=True)),
    ], null=True, blank=True)

    aside = StreamField([
        ('heading', blocks.CharBlock(classname="full title", null=True, blank=True)),
        ('paragraph', blocks.RichTextBlock(null=True, blank=True)),
        ('image', ImageChooserBlock(null=True, blank=True)),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [ StreamFieldPanel('body'), StreamFieldPanel('aside') ]


class ContactPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title",icon="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image")),
        ('two_columns', TwoColumnBlock()),
        ('embedded_video', EmbedBlock(icon="media")),
        ('google_map', GoogleMapBlock()),
    ],null=True,blank=True)

    aside = StreamField([
        ('heading', blocks.CharBlock(classname="full title", null=True, blank=True)),
        ('paragraph', blocks.RichTextBlock(null=True, blank=True)),
        ('image', ImageChooserBlock(null=True, blank=True)),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [ StreamFieldPanel('body'), StreamFieldPanel('aside') ]
