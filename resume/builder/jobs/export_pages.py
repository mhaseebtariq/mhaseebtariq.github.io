from django.template.loader import render_to_string


DETAILS_PAGES = [
    'details_gfm.html',
    'details_raven.html',
    'details_recommender.html',
]


def run():
    html = render_to_string('home.html', {'offline': False})
    with open('../index.html', 'w') as fl:
        fl.write(html)

    html = render_to_string('home.html', {'offline': True})
    with open('../offline.html', 'w') as fl:
        fl.write(html)

    for page in DETAILS_PAGES:
        html = render_to_string(page, {'offline': False})
        with open(f'../{page}', 'w') as fl:
            fl.write(html)
