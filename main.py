

def geo_logs_rus(geo_logs):
    #geo_logs = [
    #  {'visit1': ['Москва', 'Россия']},
    #  {'visit2': ['Дели', 'Индия']},
    #  {'visit3': ['Владимир', 'Россия']},
    #  {'visit4': ['Лиссабон', 'Португалия']},
    #  {'visit5': ['Париж', 'Франция']},
    #  {'visit6': ['Лиссабон', 'Португалия']},
    #  {'visit7': ['Тула', 'Россия']},
    #  {'visit8': ['Тула', 'Россия']},
    #  {'visit9': ['Курск', 'Россия']},
    #  {'visit10': ['Архангельск', 'Россия']}
    # ]
    rus_list = list()

    for visit in geo_logs:
        for city, country in visit.values():
            if country == 'Россия':
                rus_list.append(visit)

    #print(type(rus_list), rus_list)
    return rus_list

def different_list(ids):
    #ids = {'user1': [213, 213, 213, 15, 213],
    #    'user2': [54, 54, 119, 119, 119],
    #    'user3': [213, 98, 98, 35]}

    list_different = list()

    for values_ids in ids.values():
        for values_ids_list in values_ids:
            if values_ids_list not in list_different:
                list_different.append(values_ids_list)
    
    #print(list_different)
    return list_different

def max_sale(stats):
    #stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

    #print(max(stats, key=stats.get))
    return max(stats, key=stats.get)
