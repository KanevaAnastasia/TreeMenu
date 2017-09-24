# TreeMenu
Данное приложение на django реализует древовидное меню.
Меню и пункты меню добавляются и редактируюся в стандартной админке django.

Пункты меню (Item) имеют следующие параметры:
- Название
- Родитель пункта меню
- Url (принимает как относительные, относительно корня домена, так и абсолютные на внешние сайты)
- К какому меню принадлежат

Для добавления меню на страницу необходимо:

Загрузить модуль:
{% load draw_menu %}

Добавить строку для отрисовки меню с указанием его имени:
{% draw_menu 'menu_name' %}


