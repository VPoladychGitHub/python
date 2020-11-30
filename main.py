# 1 Реализовать функию parse   1111

# assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
# assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
# assert parse('http://example.com/') == {}
# assert parse('http://example.com/?') == {}
# assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse(in_str):
    res_dict: dict = dict()
    m_1 = in_str.split('?')
    if len(m_1) > 1:
        result_str = m_1[1]
        mass_param = result_str.split('&')
        l = len(mass_param[0])
        if len(mass_param[0]) > 1:
            for in_ms in mass_param:
                if len(in_ms) > 1:
                    par_mas = in_ms.split('=')
                    res_dict[par_mas[0]] = par_mas[1]

    return res_dict


print(parse('https://example.com/path/to/page?name=ferret&color=purple'))
print(parse('https://example.com/path/to/page?name=ferret&color=purple&'))
print(parse('http://example.com/'))
print(parse('http://example.com/?'))
print(parse('http://example.com/?name=Dima'))




# Реализовать функию parse_cookie (см. модуль main.py),
# Написать дополнительно 10 тестов к ней. Создать Пул реквест в ветку мастер с решением.
#    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

def parse_cookie(in_str):
    res_dict: dict = dict()
    m_1_par = in_str.split(';')
    if len(m_1_par) > 1:
        first_par = m_1_par[0]
        par_mas = first_par.split('=')
        name = par_mas[0]
        ln = len(first_par)
        ln_2 = len(name)
        sec_par = first_par[ln_2 + 1: ln]
        res_dict[name] = sec_par
        for i in range(1, len(m_1_par) - 1):
            m_i = m_1_par[i]
            mas = m_i.split('=')
            res_dict[mas[0]] = mas[1]
    return res_dict


print("----- zadaca 2 ------------")
print(parse_cookie('name=Dima;age=28;'))
print(parse_cookie(''))
print(parse_cookie('name=Dima;age=28;'))
print(parse_cookie('name=Dima=User;age=28;'))
