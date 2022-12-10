"""ask URL Configuration

The `urlpatterns` list routes URLs to q_views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function q_views
    1. Add an import:  from my_app import q_views
    2. Add a URL to urlpatterns:  path('', q_views.home, name='home')
Class-based q_views
    1. Add an import:  from other_app.q_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.q_views import Qlist, Qview, Qcreate, Qupdate, Qdelete
from webapp.c_views import c_create, c_update, c_delete
from webapp.a_view import a_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Qlist.as_view(), name='qindex'),
    path('question/<int:pk>/', Qview.as_view(), name='detailq'),
    path('question/create/', Qcreate.as_view(), name='qcreate'),
    path('question/<int:pk>/update/', Qupdate.as_view(), name='qupdate'),
    path('question/<int:pk>/delete/', Qdelete.as_view(), name='qdelete'),
    path('question/<int:pk>/choice/create/', c_create.as_view(), name="c_create"),
    path('question/<int:pk>/choice/delete/', c_delete.as_view(), name="c_delete"),
    path('question/<int:pk>/choice/update/', c_update.as_view(), name="c_update"),
    path('question/<int:pk>/answer/', a_index.as_view(), name='a_index'),
]
