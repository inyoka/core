from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class BlogIndexPage(Page):
    intro = StreamField([
        ('heading', blocks.CharBlock(classname="full title", null=True, blank=True)),
        ('paragraph', blocks.RichTextBlock(null=True, blank=True)),
        ('image', ImageChooserBlock(null=True, blank=True)),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [ StreamFieldPanel('intro') ]
