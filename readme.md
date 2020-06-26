# python-django 學習紀錄
(from python新手使用 django架站技術實作)<br>

#### 安裝指令
```
python -m pip install Django
```
<br>

#### 創建專案
```
django-admin startproject {project_name}
```

<br>
#### 啟動專案(先進到專案的資料夾中)
```
python manage.py startapp mainsite
```

<br>
#### 開啟server服務
```
python manag.py runserver
```

<br>
#### 設定sql
```
python manage.py makemigrations
python manage.py migrate
```

<br>
#### 啟用admin管理介面
```
python manage.py createsuperuser
```