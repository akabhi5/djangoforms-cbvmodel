CRUD operation using class based views (model form)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

using -

from django.views.generic.edit import CreateView, UpdateView, DeleteView
  CreateView, UpdateView, DeleteView

from django.views.generic import ListView
  ListView


- we have to give get_absolute_url in models.py so that if new row is created/new instance of model has created/CreateView has performed then that url will be triggered. Its good to use reverse so that dynamic URL could be generated and that same object can also be opened.

- default context name in case of ListView is object_list because it gives list values
- default context name in case of DeleteView(or other view which only gives just single object like DetailView) is object becuase it gives single values

- we have to provide value for var success_url in views.py so that provided URL will be triggered while deleting that particular instance
- and in this case use reverse_lazy so that operation will be performed after successful deletion only

- we do not need to mention action="" arg in these type of forms


- URL may contain any string to differentiate with other urls (like this)
      path('update/<int:pk>/', views.PersonUpdateView.as_view(), name='update'),
      path('delete/<int:pk>/', views.PersonDeleteView.as_view(), name='delete'),

      we are using update/  and  delete/

  to provide url to these link use name="..." argument

  e.g. :   {% url 'update' %}
  this will automatically take you to : localhost/update/1
    1 = is primary key of a particular instance (may change for another instance)
