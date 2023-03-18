from collections import namedtuple


Cars = namedtuple('Cars', ['name', 'owner', 'cabriolet', 'speed'])
Cars.__new__.__defaults__ = (None, None, False, None)


def test_car_asdict():
    t_cars = Cars('LaFerrari', 'Mario', False, 305)
    t_dict = t_cars._asdict()
    expected = {'name':'LaFerrari',
                'owner':'Mario',
                'cabriolet':False,
                'speed':305}
    assert t_dict == expected


def test_owner_replace():
    t_before = Cars('VAZ2108','Semen', False)
    t_after = t_before._replace(owner='Oleg', cabriolet=True, speed=85)
    t_expected = Cars('VAZ2108', 'Oleg', True, 85)
    assert t_after == t_expected


