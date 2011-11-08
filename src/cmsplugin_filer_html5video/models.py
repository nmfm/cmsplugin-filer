# coding: utf-8
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.video import FilerVideoField
from os.path import basename

class Html5Video(CMSPlugin):
    # player settings
    movie = FilerVideoField(verbose_name=_('video file'), help_text=_('use .flv file or h264 encoded video file'))

    def __unicode__(self):
        return u"%s" % basename(self.movie.path)

    #def get_height(self):
        #return "%s" % (self.height)
    
    #def get_width(self):
        #return "%s" % (self.width)    
    
    #def get_movie(self):
        #if self.movie:
            #return self.movie.url
        #else:
            #return self.movie_url

