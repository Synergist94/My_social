1 этап: УСТАНОВКА DJANGO и создание проекта с приложением<br>
    *создадим на рабочем столе папку с названием проекта<br>
    *Откроем папку в vs code<br>
    *vs code  откроем терминал и напишем python -m venv venv<br>
        (Данная команда создает виртуальную среду для разработки)<br>
    *Далее активируем ее с помощью этой команды venv/Scripts/activate.ps1<br>
    *В активированную среду разработки установим DJANGO командой pip install django<br>
    *Для того чтобы каждый раз не писать зановой команду установки django пропишем такую команду pip freeze > Имя документа.txt(в моем случае это sett_pip.txt)
    *создадим проект командой django-admin startproject название проекта .<br>
        (в моем случае это app) через пробел ставим точку, для того что бы не создалась лишняя папка допусти без точки будет выглядеть так(папка на рабочем столе/app/app/(тут структура проеута)), точка служит для того чтобы убрать одну папку пример (папка на рабочем стале/app/(структура проекта))<br>
    *Далее создадим приложение users в нем мы будем реализовывать такие функции как (авторизация, регистрация,профиль,стена,лента и тд)
