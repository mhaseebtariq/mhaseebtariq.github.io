from django.template.loader import render_to_string


def run():
    html = render_to_string('home.html', {'offline': False})
    with open('../index.html', 'w') as fl:
        fl.write(html)

    html = render_to_string('home.html', {'offline': True})
    with open('../offline.html', 'w') as fl:
        fl.write(html)

    html = render_to_string('details_raven.html', {'offline': False})
    with open('../details_raven.html', 'w') as fl:
        fl.write(html)
