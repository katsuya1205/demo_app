from django.urls import path
from . import views# 同じ階層のviews.pyを読み込む、という意味

urlpatterns = [
path("", views.index, name="index")
]# views.pyには様々な関数が入っている。関数indexを呼び出した。
