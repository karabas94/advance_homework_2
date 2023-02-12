from urllib.parse import urlparse, parse_qsl


def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    """
    This function return parsed cookie to dictionary
    """
    return dict(parse_qsl(query, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace',
                          max_num_fields=None, separator=';'))


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;;age=28') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie(';name=Dima=User;age=28') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie(';name=Dima=User;;age=28;&=123') == {'name': 'Dima=User', 'age': '28', '&': '123'}
    assert parse_cookie(';name=Dima=User;?;age=28;&=&?123') == {'name': 'Dima=User', 'age': '28', '&': '&?123'}
    assert parse_cookie('name=;age=;color=') == {}
    assert parse_cookie('=Dima;=28;=purple') == {'': 'purple'}
    assert parse_cookie('name=Dima;=28;=purple') == {'name': 'Dima', '': 'purple'}
    assert parse_cookie('name=Dima;age;=28;=purple') == {'name': 'Dima', '': 'purple'}
    assert parse_cookie('=Dima;age=28;=purple') == {'': 'purple', 'age': '28'}
    assert parse_cookie('=Dima;age=28;color=+') == {'': 'Dima', 'age': '28', 'color': ' '}
