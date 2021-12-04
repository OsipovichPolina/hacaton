# Форус

# 1. Обработка данных
Изначально мы визуализировали исходные данные на BI мониторе.

Затем в файле "Catboost.ipynb" мы обрабатывали данные: 
1) Получали категории, если в строках их не было
2) Формализовали версию ос
3) Улучшили категории
4) Определили локальное время вместо Московского, а также категоризовали его

# 2. Классификация
В файле "Catboost_final.ipynb" мы обучили модель при помощи библиотеки Яндекса Catboost, затем предсказали сегмент на тестовой выборке
Результат можно видеть в csv файле "test_pred.csv" в архиве "test_pred.zip" по ссылке https://drive.google.com/file/d/1x9xGbgZmrWQ_82vUZ66YZCjsp4KHVPez/view?usp=sharing

# 3. Переход от фактов к ролям(людям)
Файл old.py

df = pd.read_csv('train.csv', sep=',')
cat = pd.read_csv('cat_dur.csv', sep=';')
В файле cat_dur.csv:
category - категория приложения
ad - время (минуты), показывающее насколько часто показывается реклама в этом типе приложений
uses - среднее время (минуты), которое пользователь тратит в этом типе приложений

В результате выполнения мы получаем сколько в каждой категории было записей всего и сколько из них мы отнесли к одному человеку.
Для сокращения времени подсчета этот результат был получен лишь для нескольких городов и версий ОС. Данные получились близкими по значению, поэтому на их основе было сформированы коэффициенты для преобразования записей к людям.

Файл clust.py
Для подсчета людей в сегменте
df = pd.read_csv('test_pred.csv', sep=',') 
coeff = pd.read_csv('coeff.csv', sep=';') - коэффиценты преобразования записей к ролям(людям)

В результате в файле people.csv видим сколько людей в каждом сегменте

# 4. Кластеризация
1) Кластеризация проходила в файле "Clustering.ipynb".
2) Брались за основу обработанные train и test данные
3) Выделялись параметры которые существенно влияют на кластеризацию
4) Проводилась обработка категориальных параметров
5) Проходила кластеризация при помощи библиотеки "scikit-learn" и метода "AgglomerativeClustering"
6) Полученные описанные результаты можно увидеть на BI мониторе и в архиве "cluster_csv.zip"

# 5. Power BI
Монитор BI на основе изначального набора данных

https://app.powerbi.com/view?r=eyJrIjoiNDZjNGJjYjctNTNlNS00NzZjLTkwNTktNmJkMDkyNTkwOWJjIiwidCI6IjM0YWVkYzA0LWNmNjAtNDhjOS1hZTM2LTYxODQ5NWI4MzdlZCIsImMiOjl9

Монитор BI на основе обработанного набора данных

https://app.powerbi.com/view?r=eyJrIjoiNzQxZDUyNDAtNGY0ZS00Y2U2LTg5YjctNDBhZGIyNTEwNjdiIiwidCI6IjM0YWVkYzA0LWNmNjAtNDhjOS1hZTM2LTYxODQ5NWI4MzdlZCIsImMiOjl9

Монитор BI визуализирующий созданные нами кластеры

https://app.powerbi.com/view?r=eyJrIjoiMWJmZWQ0NGEtZGI0OS00ZWZlLWI3MDctYmJmNzgxZTNmNjZlIiwidCI6IjM0YWVkYzA0LWNmNjAtNDhjOS1hZTM2LTYxODQ5NWI4MzdlZCIsImMiOjl9
