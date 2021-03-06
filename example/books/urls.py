
from django.conf.urls.defaults import *
import views, models, forms


urlpatterns = patterns('djpclient_example.views',
    url(r'^authors/$', views.list_and_add_view,
        {'template_name': 'authors.html',
         'model': models.Author,
         'formclass': forms.AuthorForm},
        name='authors'),
    
#    url(r'^books/$', views.list_and_add_view,
#        {'template_name': 'books.html',
#         'model': models.Book,
#         'formclass': forms.BookForm},
#        name='books'),
     
    url(r'^books/$', views.book_view, name='books'),
    
    url(r'^publishers/$', views.list_and_add_view,
        {'template_name': 'publishers.html',
         'model': models.Publisher,
         'formclass': forms.PublisherForm},
        name='publishers'),
    
    url(r'^angular-list/$', views.show_template,
        {'template_name': 'angular-list.html'},
        name='angular-list'),
    
    url(r'^angular-projects/$', views.show_template,
        {'template_name': 'angular-projects.html'},
        name='angular-projects'),
)

