# -*- coding: utf-8 -*-
from django.db import models


class CacheKeyManager(models.Manager):
    def get_keys(self, site_id=None, language=None):
        ret = self.none()
        if not site_id and not language:
            # Both site and language are None - return everything
            ret = self.all()
        elif not site_id:
            ret = self.filter(language=language)
        elif not language:
            ret = self.filter(site=site_id)
        else:
            # Filter by site_id *and* by language.
            ret = self.filter(site=site_id).filter(language=language)
        return ret

    def get_or_create(self, **kwargs):
        try:
            return super(CacheKeyManager, self).get_or_create(**kwargs)
        except CacheKey.MultipleObjectsReturned:
           
            CacheKey.objects.all().delete()
            return super(CacheKeyManager, self).get_or_create(**kwargs)

class CacheKey(models.Model):

    language = models.CharField(max_length=255)
    site = models.PositiveIntegerField()
    key = models.CharField(max_length=255)
    objects = CacheKeyManager()
