from main import geo_logs_rus, different_list, max_sale
import pytest

class Test_Func:
    @pytest.mark.parametrize(
        "geo_logs, expected", [
            ([{'visit1': ['Москва', 'Россия']},
             {'visit2': ['Дели', 'Индия']},
             {'visit3': ['Владимир', 'Россия']},
             {'visit4': ['Лиссабон', 'Португалия']}], [{'visit1': ['Москва', 'Россия']},
                                                       {'visit3': ['Владимир', 'Россия']}]),
            ([{'visit1': ['Москва', 'Россия']},
              {'visit2': ['Дели', 'Индия']},
              {'visit4': ['Лиссабон', 'Португалия']}], [{'visit1': ['Москва', 'Россия']}]),
            ([{'visit1': ['Москва', 'Россия']},
              {'visit2': ['Тула', 'Россия']},
              {'visit3': ['Владимир', 'Россия']},
              {'visit4': ['Лиссабон', 'Португалия']}], [{'visit1': ['Москва', 'Россия']},
                                                        {'visit2': ['Тула', 'Россия']},
                                                        {'visit3': ['Владимир', 'Россия']}])
        ]
    )
    def test_geo_logs_rus(self, geo_logs, expected):
        result = geo_logs_rus(geo_logs)
        assert result == expected

    @pytest.mark.parametrize(
        "ids, expected", [
           ({'user1': [213, 213, 213, 15, 213],
            'user2': [54, 54, 119, 119, 119],
            'user3': [213, 98, 98, 35]}, [213, 15, 54, 119, 98, 35]),
            ({'user1': [213, 213, 213],
             'user2': [54, 119, 119],
             'user3': [98]}, [213, 54, 119, 98]),
            ({'user1': [213, 15, 213],
             'user2': [54, 54],
             'user3': [98, 98]}, [213, 15, 54, 98])
        ]
    )
    def test_different_list(self, ids, expected):
        result = different_list(ids)
        assert result == expected

    @pytest.mark.parametrize(
        "stats, expected", [
           ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
           ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 140, 'email': 42, 'ok': 98}, 'google'),
           ({'facebook': 155, 'yandex': 120, 'vk': 115, 'google': 140, 'email': 42, 'ok': 98}, 'facebook')
        ]
    )
    def test_max_sale(self, stats, expected):
        result = max_sale(stats)
        assert result == expected
