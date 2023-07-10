```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('result/', views.result, name='result'),
    path('detail/<int:doc_id>/', views.detail, name='detail'),
]
```