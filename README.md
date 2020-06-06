# my_blog
Relearn Django framework by constructing a blog app step by step



Notes：

之前做过几个课程项目使用的都是Django框架，但是都有一些拿来主义的感觉，没有对这个框架进行深入的了解，这里碰巧发现一个蛮不错的教程，在此重新跟着教程重新码一遍代码。

参考：

https://www.dusaiphoto.com/article/detail/2/

* 进度

### day1： 搭建开发环境(git 目录  my_blog project目录   app 目录)

```python
# 创建project 
>django-admin startproject my_blog
# 查看效果
>cd my_blog 
>python manage.py runserver

# 创建APP
>python manage.py startapp article

# 注册APP（settings）
my_blog/settings.py
INSTALLED_APPS = [
    ...,
    'article',
]

# 配置访问路径（urls）
my_blog/urls.py
urlpatterns = [
    ...,
    path('article/', include('article.urls', namespace='article')),
]

article/urls.py (新建一个urls.py)
from django.urls import path
app_name = 'article'
urlpatterns = [
    # 后续views中的函数url
]

```

