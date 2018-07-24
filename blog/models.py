from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index


class BlogIndexPage(Page):
    intro = StreamField([
        ('heading', blocks.CharBlock(classname="full title", null=True, blank=True)),
        ('paragraph', blocks.RichTextBlock(null=True, blank=True)),
        ('image', ImageChooserBlock(null=True, blank=True)),
    ], null=True, blank=True)

    aside = StreamField([
        ('heading', blocks.CharBlock(classname="full title", null=True, blank=True)),
        ('paragraph', blocks.RichTextBlock(null=True, blank=True)),
        ('image', ImageChooserBlock(null=True, blank=True)),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('intro'),
        StreamFieldPanel('aside')
    ]

    # def get_context(self, request):
    #     context = super(BlogIndexPage, self).get_context(request)
    #     context['blog_index'] = BlogIndexPage.objects.first()
    #     return context

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    def __str__(self):
        return f'{self.into}'


class BlogPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock(null=True, blank=True)),
        ('image', ImageChooserBlock(null=True, blank=True)),
    ], null=True, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]
