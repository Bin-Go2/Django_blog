

假设这里返回的网页内容从数据库取出
所以已经预设了开发者在app_name/admin中对数据表进行了注册
admin.site.register(...)


1.在views.py中编写视图函数  return render(request, 'article/list.html', context) 
2.配置URLconfs，将用户请求的URL链接关联起来（将用于在浏览器中输入的地址映射到对应的视图函数）
3.用户访问


render函数的作用：
render(request,模板文件的位置、名称,context)
结合模板和上下文，并返回渲染后的HttpResponse对象。通俗的讲就是把context的内容，加载进模板，并通过浏览器呈现




## settings.py中需要进行配置的一些文件


templates目录：模板文件在项目根目录的templates文件夹（自己手动创建）
static目录: 模板文件在项目根目录的static文件夹（自己手动创建）



```
my_blog  - 项目目录 settings.py中的BASE_DIR  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
│  ...
├─article - app目录，settings.py中INSTALLED_APPS = ['article',] 定义
│  ...
└─my_blog - 项目容器目录,包含包含项目的配置信息 settings.py在其中
│  ...
└─templates - 模板目录 settings.py中需要声明 TEMPLATES = [ ...,'DIRS': [os.path.join(BASE_DIR, 'templates')], ...}
└─static    - 静态文件目录 settings.py中需要声明 STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
    └─bootstrap
    │   ├─css # 文件夹
    │   └─js # 文件夹
    └─jquery
    └─popper

 
```


## 如何使用静态文件
html中要加上 {% load static %} 之后，才可使用 {% static 'path' %} 引用静态文件。
path对应静态文件的位置 例如 <script src="{% static 'bootstrap/js/bootstrap.min.js' %}"></script> 表明bootstrap.min.js位置在BASE_DIR/STATICFILES_DIRS/bootstrap/js/bootstrap.min.js