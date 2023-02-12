from urllib.parse import urlparse, parse_qsl


def parse(query: str) -> dict:
    """
    This function return parsed query string to dictionary
    """
    return dict(parse_qsl(urlparse(query).query))


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=?ferret&color=purple&') == {'name': '?ferret',
                                                                                    'color': 'purple'}
    assert parse("https://www.youtube.com/watch?v=K8_ov_bsyNA&t=8832s") == {'v': 'K8_ov_bsyNA', 't': '8832s'}
    assert parse(
        "https://www.google.com/search?q=maritime+zone&oq=maritime+zo&aqs=chrome&sourceid=chrome&ie=UTF-8") == {
               'q': 'maritime zone', 'oq': 'maritime zo', 'aqs': 'chrome', 'sourceid': 'chrome', 'ie': 'UTF-8'}
    assert parse("https://www.google.com/search?q=%3Fwhy%26not%3Fyou&sxsrf=AJOq&?=i9b") == {'q': '?why&not?you',
                                                                                            'sxsrf': 'AJOq', '?': 'i9b'}
    assert parse("https://open.spotify.com/track/6xnYEyui?=Qt3LaY_ZqLg&=sdfs&=dfds") == {'': 'dfds'}
    assert parse("https://open.spotify.com/track/6xnYEyui?Qt3LaY_ZqLg=&sdfs=&dfds=") == {}
    assert parse("https://open.spotify.com/track/6xnYEyui?Qt3LaY_ZqLg=&sdfs=&dfds=joJuoj&") == {'dfds': 'joJuoj'}
    assert parse(
        "https://www.google.com/search?q=parse+cookie+urllib&oq=&aqs=chrome?0?35i39i362l8?1539&sourceid=chrome&ie=UTF-8") == {
               'q': 'parse cookie urllib', 'aqs': 'chrome?0?35i39i362l8?1539', 'sourceid': 'chrome', 'ie': 'UTF-8'}
    assert parse(
        "https://www.google.com/search?q=parse+cookie+urllib&oq=&aqs=chrome465&353&5623?&sour&&ceid=chrome&ie=UTF-8") == {
               'q': 'parse cookie urllib', 'aqs': 'chrome465', 'ceid': 'chrome', 'ie': 'UTF-8'}
    assert parse("https://www.youtube.com/watch?v=b2j9z?&?L2Tau0") == {'v': 'b2j9z?'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
