# **CleanBlog**

## **Блог на основе Django**


### Для начала необходимо скачать зависимости:


.. code:: bash

    pip install asgiref==3.5.0
  
    pip install Django==4.0.4
  
    pip install sqlparse==0.4.2
  



## Инструкция по запуску:


1.Клонировать/Скачать репозиторий:

.. code:: bash
   git clone https://github.com/CleanBlog

2. Перейти в директорию со скачанным репозиторием:

.. code:: bash
   cd ../CleanBlog

3. Запустить виртуальную среду:

.. code:: bash
  CleanBlog$ source venv/bin/activate

4. Перейти в наше приложение mysite внутри папки CleanBlog:

.. code:: bash
  CleanBlog$ cd mysite

5. Запустить сервер:

.. code:: bash
  mysite$ python manage.py runsrver

### Чтобы перейти в админку необходимо:
1. Дописать к URL: ../admin
2. Вести логин/пароль: admin/admin

### Чтобы добавить пост:
1. Перейти на админку
2. Нажать на “+post”

### Чтобы изменить страничку о нас(about):
1. Перейти в админку
2. Нажать на “+about”

### На этом все.
