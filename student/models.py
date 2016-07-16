from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Document(models.Model):
    TYPE_CHOICES = (
            (1, _('type1')),
            (2, _('type2')),
            (3, _('type3')),
    )

    name = models.CharField(max_length=50, verbose_name= _('document name'))
    slug = models.SlugField(_('slug document'), help_text=_('Use ascii characters'))
    description = models.TextField(_('description'), blank=True)
    image = models.ImageField(_('document image'), blank=True)
    document_file = models.FileField(_('document file'), blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('insert time'))
    is_free = models.BooleanField(default=True,verbose_name= _('is document free'))
    price = models.PositiveIntegerField(verbose_name=_('price'), default=0)
    document_type = models.PositiveSmallIntegerField(verbose_name= _('document name'), choices= TYPE_CHOICES)

    class Meta:
        db_table = "document"
        verbose_name = _('documents')
        verbose_name_plural = _('Documents')
        ordering = ["name"]    

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100, verbosename=_('headline for news'))
    description = models.TextField(_('news details'), blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('insert time'))
    image = models.ImageField(_('document image'), blank=True)
    news_file = models.FileField(_('document file'), blank=True)
    is_show = models.BooleanField(default=True,verbose_name= _('show news'))
    
    class Meta:
        db_table = "news"
        verbose_name = _('news')
        verbose_name_plural = _('news')
        ordering = ["title"]    

    def __str__(self):
        return self.title

class Consultant(models.Model):
    TYPE_CHOICES = (
            (1, _('type1')),
            (2, _('type2')),
            (3, _('type3')),
    )
    name = models.CharField(max_length=50, verbose_name= _('consultant name'))
    degree = models.PositiveSmallIntegerField(verbose_name= _('consultant degree'), choices= TYPE_CHOICES)
    image = models.ImageField(_('consultant image'), blank=True)
    news_file = models.FileField(_('consultant file'), blank=True)
    
    class Meta:
        db_table = "consultant"
        verbose_name = _('consultant')
        verbose_name_plural = _('consultant')
        ordering = ["name"]    

    def __str__(self):
        return self.name








