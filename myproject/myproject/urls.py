# from django.conf.urls import patterns, include, url

# # Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'myproject.views.home', name='home'),
#     # url(r'^myproject/', include('myproject.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )



# # -*- coding: utf-8 -*-
# from django.conf.urls import patterns, include, url
# from django.conf import settings
# from django.conf.urls.static import static
# #from django.views.generic.simple import redirect_to
# from django.views.generic import TemplateView

# urlpatterns = patterns('',
# 	url(r'^admin/', include(admin.site.urls)),
# 	(r'^myapp/', include('myapp.urls')),
# 	# (r'^$', redirect_to, {'url': '/myapp/list/'}), # Just for ease of use.
#     # (r'^$', TemplateView.as_view(template_name="list.html")),
#     (r'^$', TemplateView.as_view(template_name="list.html")),
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    (r'^', include('myapp.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)