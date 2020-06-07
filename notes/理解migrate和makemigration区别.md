## 理解migrate和makemigration区别


`
python manage.py makemigrations  （数据的改动记录）
` 
Django 在  app_name/migrations下生成了一个 0001_initial.py 文件，用于记录对模型做了哪些修改，
但这只是告诉Django对于模型做了哪些改变，改动还没有作用到数据库文件


`python manage.py migrate （数据的改动实现）
`
Django 通过检测app_name/migrations下的文件，得知数据库做了哪些操作，然后把这些操作翻译成数据库操作语言，从而把这些操作作用于真正的数据库



一般项目刚创建的时候会自动生成一些数据表，通过`python manage.py migrate` 生成一个’空’的数据库（里面有一些自带的表）

在开发工程中建表，
1.首先去models里面新建类
2.执行`python manage.py makemigrations`
3.执行`python manage.py migrate`
