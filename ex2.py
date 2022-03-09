

def passport(**kwargs):
    el_list = []
    for el in kwargs.values():
        el_list.append(el)
    print(*el_list)

passport(name_u = input(), surname_u = input(), year_u = input(), city_u = input(), email_u = input(), phone_u = input())