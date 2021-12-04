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
Результат можно видеть в csv файле "test_pred.csv" в архиве "test_pred.zip"

# 3. Переход от фактов к ролям(людям)

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
