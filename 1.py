import pandas as pd
# Чтение данных
data = pd.read_csv("kc_house_data.csv")
# Просмотр первых 5 строк
print(data.head())
# Описание столбцов и их содержимого
print(data.info())
# Проверка на пропуски
print(data.isnull().sum())
# Основные статистики
print(data.describe())

# Проверка типов данных
print(data.dtypes)
# Поиск пропущенных данных
print(data.isnull().sum())
# Основные статистики
print(data.describe())
# Анализ диапазонов значений
print("Диапазон цен:", data['price'].min(), "-",
data['price'].max())
print("Диапазон жилой площади:", data['sqft_living'].min(), "-",
data['sqft_living'].max())
# Исследование категориальных признаков
print(data['waterfront'].value_counts())
print(data['view'].value_counts())
print(data['condition'].value_counts())
print(data['grade'].value_counts())

# Диапазон стоимости недвижимости
price_range = data['price'].min(), data['price'].max()
print("Диапазон стоимости недвижимости:", price_range)
# Доля жилой площади от общей площади
data['living_ratio'] = data['sqft_living'] / data['sqft_lot']
average_living_ratio = data['living_ratio'].mean()
print("Средняя доля жилой площади:", average_living_ratio)
# Количество домов с разным количеством этажей
floors_distribution = data['floors'].value_counts()
print("Распределение домов по этажам:", floors_distribution)
# Состояние домов
average_condition = data['condition'].mean()
print("Среднее состояние домов:", average_condition)
# Года постройки первого и последнего дома
yr_built_range = data['yr_built'].min(), data['yr_built'].max()
print("Года постройки первого и последнего дома:", yr_built_range)

# Средняя стоимость домов с 2 спальнями
average_price_2_bedrooms = data[data['bedrooms'] ==
2]['price'].mean()
print("Средняя стоимость домов с 2 спальнями:",
average_price_2_bedrooms)
# Средняя площадь домов с ценой выше 600000
average_sqft_living_expensive = data[data['price'] >
600000]['sqft_living'].mean()
print("Средняя площадь дорогих домов:",
average_sqft_living_expensive)
# Количество домов с ремонтом
renovated_houses_count = data[data['yr_renovated'] > 0].shape[0]
print("Количество домов с ремонтом:", renovated_houses_count)
# Сравнение стоимости домов с разными оценками
average_price_high_grade = data[data['grade'] >
10]['price'].mean()
average_price_low_grade = data[data['grade'] < 4]['price'].mean()
price_difference = average_price_high_grade - average_price_low_grade
print("Разница в стоимости между домами с высокой и низкойоценкой:", price_difference)

# Фильтрация домов по запросу клиента
client_houses_1 = data[(data['waterfront'] == 1) &
(data['bathrooms'] >= 3) & (data['sqft_basement'] > 0)]
# Количество подходящих домов
num_houses_client_1 = client_houses_1.shape[0]
print("Количество домов, подходящих клиенту (1):",
num_houses_client_1)
client_houses_2 = data[((data['view'] > 0) | (data['waterfront']
== 1)) &
(data['condition'] >= 4) &
(data['yr_built'] >= 1980)]
# Определение ценового диапазона
price_range_client_2 = (client_houses_2['price'].min(),
client_houses_2['price'].max())
print("Ценовой диапазон подходящих домов (2):",
price_range_client_2)
# Фильтрация домов по запросу клиента
client_houses_3 = data[(data['sqft_basement'] == 0) &
(data['floors'] == 2) &
(data['price'] <= 150000)]
# Средняя оценка по состоянию
average_condition_client_3 = client_houses_3['condition'].mean()
print("Средняя оценка по состоянию домов, подходящих клиенту(3):", average_condition_client_3)

import pandas as pd
# Чтение данных
data = pd.read_csv("kc_house_data.csv")
# Просмотр первых 5 строк
print(data.head())
# Описание столбцов и их содержимого
print(data.info())
# Проверка на пропуски
print(data.isnull().sum())
# Основные статистики
print(data.describe())
# Проверка типов данных
print(data.dtypes)
# Поиск пропущенных данных
print(data.isnull().sum())
# Основные статистики
print(data.describe())
# Анализ диапазонов значений
print("Диапазон цен:", data['price'].min(), "-",
data['price'].max())
print("Диапазон жилой площади:", data['sqft_living'].min(), "-",
data['sqft_living'].max())
# Исследование категориальных признаков
print(data['waterfront'].value_counts())
print(data['view'].value_counts())
print(data['condition'].value_counts())
print(data['grade'].value_counts())
# Диапазон стоимости недвижимости
price_range = data['price'].min(), data['price'].max()
print("Диапазон стоимости недвижимости:", price_range)
# Доля жилой площади от общей площади
data['living_ratio'] = data['sqft_living'] / data['sqft_lot']
average_living_ratio = data['living_ratio'].mean()
print("Средняя доля жилой площади:", average_living_ratio)
# Количество домов с разным количеством этажей
floors_distribution = data['floors'].value_counts()
print("Распределение домов по этажам:", floors_distribution)
# Состояние домов
average_condition = data['condition'].mean()
print("Среднее состояние домов:", average_condition)
# Года постройки первого и последнего дома
yr_built_range = data['yr_built'].min(), data['yr_built'].max()
print("Года постройки первого и последнего дома:", yr_built_range)
# Средняя стоимость домов с 2 спальнями
average_price_2_bedrooms = data[data['bedrooms'] ==
2]['price'].mean()
print("Средняя стоимость домов с 2 спальнями:",
average_price_2_bedrooms)
# Средняя площадь домов с ценой выше 600000
average_sqft_living_expensive = data[data['price'] >
600000]['sqft_living'].mean()
print("Средняя площадь дорогих домов:",
average_sqft_living_expensive)
# Количество домов с ремонтом
renovated_houses_count = data[data['yr_renovated'] > 0].shape[0]
print("Количество домов с ремонтом:", renovated_houses_count)
# Сравнение стоимости домов с разными оценками
average_price_high_grade = data[data['grade'] >
10]['price'].mean()
average_price_low_grade = data[data['grade'] < 4]['price'].mean()
price_difference = average_price_high_grade - average_price_low_grade
print("Разница в стоимости между домами с высокой и низкой оценкой:", price_difference)
# Фильтрация домов по запросу клиента
client_houses_1 = data[(data['waterfront'] == 1) &
(data['bathrooms'] >= 3) & (data['sqft_basement'] > 0)]
# Количество подходящих домов
num_houses_client_1 = client_houses_1.shape[0]
print("Количество домов, подходящих клиенту (1):",
num_houses_client_1)
client_houses_2 = data[((data['view'] > 0) | (data['waterfront']
== 1)) &
(data['condition'] >= 4) &
(data['yr_built'] >= 1980)]
# Определение ценового диапазона
price_range_client_2 = (client_houses_2['price'].min(),
client_houses_2['price'].max())
print("Ценовой диапазон подходящих домов (2):",
price_range_client_2)
# Фильтрация домов по запросу клиента
client_houses_3 = data[(data['sqft_basement'] == 0) &
(data['floors'] == 2) &
(data['price'] <= 150000)]
# Средняя оценка по состоянию
average_condition_client_3 = client_houses_3['condition'].mean()
print("Средняя оценка по состоянию домов, подходящих клиенту(3):", average_condition_client_3)