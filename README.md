# project

параметры редактированяи записей в базах данных по запросу


Адрес для запроса на просмотр и на создание новой записи.
127.0.0.1:5000/department
127.0.0.1:5000/worker
GET запрос - Просмотр всех записей
POST - создание новой


Адреса для просмсотра и редактирования отдельных записей в таблице: 
в конце адреса добавлен ID записи для обработки. 
127.0.0.1:5000//department/<department_id>')
127.0.0.1:5000//worker/<worker_id>')

GET запрос - Просмотр всех записей
PUT - Редактирование 
DELETE - удаление записи. 

#Отделы
имя отдела : department

#workers
department_id - id номер отдела
fullname - полное имя сотрудника
birthday - дата дня рождения
salary - ЗП

# filter by birthday
запрос get к выводу списка сотрдуников 127.0.0.1:5000/worker
birthday_begin - нижний предел
birthday_end - верхний предел 

Пример запроса CURL : 
  curl http://127.0.0.1:5000/worker/9 -d "fullname=oleg Bagdanovich" -d "birthday=1990-05-09" -d "department_id=5" -d "salary=222" -X PUT -v

пример фильтра CURL : 
  curl http://127.0.0.1:5000/worker -d "birthday_begin=1990-01-01" -d "birthday_end=1992-01-01"  -X GET -v
