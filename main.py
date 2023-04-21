import pytest

def task_1(geo_logs):

    geo_log = []
    CONST = 'Россия'

    for visit in geo_logs:
        country = list(visit.values())[0][1]
        if country == CONST:
            geo_log.append(visit)

    return geo_log


def task_2(ids):
    set_1 = set()

    for l in ids.values():
        set_1 = set(l) | set_1

    list_1 = list(set_1)

    return(list_1)


def task_3(queries):
    l = len(queries)
    dict = {1: 0, 2: 0, 3: 0}

    for request in queries:
        req = request.split()
        len_req = len(req)
        dict[len_req] += 1
    i = 0

    res ={}

    for request in dict:
        req_percent = dict.get(request) * 100 / l
        if req_percent != 0:
            res[request] = round(req_percent, 2)

    return res

@pytest.mark.parametrize("x, expected", [
    (
        [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']},
        ], [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
    )
])
def test_task_1(x, expected):
    res = task_1(x)
    assert res == expected



@pytest.mark.parametrize("x, expected", [
    (
        {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]},

        [98, 35, 213, 54, 119, 15]
    )
])
def test_task_2(x, expected):
    res = task_2(x)
    assert res == expected

@pytest.mark.parametrize("x, expected", [
    (
        [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
        ],
        {2: 42.86, 3: 57.14}
    )
])
def test_task_3(x, expected):
    res = task_3(x)
    assert res == expected

#для запуска:   python -m pytest main.py