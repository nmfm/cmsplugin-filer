import os
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cmsplugin_filer_html5video.models import Html5Video
from cmsplugin_filer_html5video.forms import Html5VideoForm
from filer.settings import FILER_STATICMEDIA_PREFIX

class Html5VideoPlugin(CMSPluginBase):
    model = Html5Video
    name = _("Video (HTML5)")
    form = Html5VideoForm

    render_template = "cmsplugin_filer_html5video/video.html"
    #text_enabled = True

    #class PluginMedia:
        #js = ('https://ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js',)

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder':placeholder,
        })
        return context

    #def icon_src(self, instance):
        #return os.path.normpath(u"%s/icons/video_%sx%s.png" % (FILER_STATICMEDIA_PREFIX, 32, 32,))
plugin_pool.register_plugin(Html5VideoPlugin)
