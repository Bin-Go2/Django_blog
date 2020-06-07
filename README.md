# Django_blog
Relearn Django framework by constructing a blog app step by step

Notes：

之前做过几个课程项目使用的都是Django框架，但是都有一些拿来主义的感觉，没有对这个框架进行深入的了解，这里碰巧发现一个蛮不错的教程，在此重新跟着教程重新码一遍代码。

参考：

https://www.dusaiphoto.com/article/detail/2/

* 进度

### day1： 搭建开发环境(git 目录  my_blog project目录   app 目录)，

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

### day2： 理解MTV模型，创建数据库，编写view.py部分代码（文章列表，详情），编写部分模板
MVT表达的意思和MVC是一样的

M = M 数据处理 => 数据库  Django通过models.py 映射到数据库 （ORM object relational mapping）
V = C 控制器 => 业务处理
T = V 视图 => 页面显示

```python

article/models.py
# 文章类
class ArticlePost(models.Model):
    ...  
    
# 数据库迁移  ->  每当对数据库进行了更改（添加、修改、删除等）操作，都需要进行数据迁移。
## 通过运行 makemigrations 命令，Django 会检测你对模型文件的修改，并且把修改的部分储存为一次迁移。
>python manage.py makemigrations
>python manage.py migrate

# 创建管理员账号，管理网站后台
>python manage.py createsuperuser

# 将ArticlePost注册到后台中, 通过注册可以将该模型交给网站后台进行管理（可以在开发阶段进行添加测试数据）
article/admin.py

from .models import ArticlePost
admin.site.register(ArticlePost)


# 编写view函数  view -> 函数 (接受request，返回response)
def article_list(request):
	...

def article_detail(request, id):
	...

# urlconf映射视图函数
path('article-list/', views.article_list, name='article_list')


base.html list.html ....
...


```
Django views are a key component of applications built with the framework. At their simplest they are a Python function or class that takes a web request and return a web response. Views are used to do things like fetch objects from the database, modify those objects if needed, render forms, return HTML, and much more.


