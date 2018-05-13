关于Django_Blog
=====================
##Based on:[django_blog](https://github.com/lzjun567/django_blog)
##demo:[xdp.space](http://xdp.space)

####我的运行环境
在树莓派上部署的blog,通过[frp](github.com/frp)映射到我的公网ip上。

####安装运行
Python版本使用3.4，首先确保系统有Python3的环境。还没安装的请移步至：[Python安装](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000)。项目的安装推荐使用virtualenv，它能提供一个完全隔离的python环境，安装virtualenv:  
    
    $ pip install --upgrade virtualenv

然后使用virtualenv创建一个python虚拟环境  

    $ mkdir ~/.virtualenvs
    $ virtualenv -p python3 ~/.virtualenvs/django_blog
激活虚拟环境django_blog  

    $ source ~/.virtualenvs/django_blog/bin/activate
如果你使用windows，运行：  

    $ ~/virtualenvs/django_blog/bin/activate    

下载安装第三方依赖包：  
    
    (django_blog) $ cd /home/${user}/workspace #你可以把project下载到任意你想放的地方
    (django_blog) $ git clone https://github.com/lzjun567/django_blog.git
    (django_blog) $ cd django_blog
    (django_blog) $ pip install -r requirements/dev.txt
    (django_blog) $ python manage.py makemigration
    (django_blog) $ python manage.py migrate
    (django_blog) $ python manage.py runserver localhost:8000

####预览效果 
![预览效果 ][1]


####开发文档
[develop.md](./doc/develop.md)

####TODO
- [x] 1.更新到django2.0
- [ ] 2.支持Markdown编写博文
- [ ] 3.引入Xadmin管理后端
- [ ] 4.编写评论系统
- [ ] 5.接入PiCenter管理我的树莓派

任何建议或者参与开发，可以[New Issue](https://github.com/lzjun567/django_blog/issues)。项目遵循[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)协议  
 
  [1]: http://foofish.qiniudn.com/v1.2.png

