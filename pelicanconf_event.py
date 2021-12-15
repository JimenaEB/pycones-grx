#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

EVENT_TITLE = "PyconES 2022"
EVENT_SUBTITLE = "Granada"
EVENT_DESCRIPTION = """
Bienvenidos a la PyConES, la conferencia nacional sobre Python más importante de España.<br>
Un evento de tres días que reunirá a los ponentes más interesantes, una agenda increíble y unas oportunidades de trabajo
maravillosas.<br>
Con tu entrada podrás acceder los dos días de la conferencia completos.<br>
Tambien puedes formar parte de nuestros patrocinadores y tener tu espacio dentro del evento.
"""

TICKETS_LINK="#"
CALL_FOR_PAPERS_LINK = "#"

# https://google-map-generator.com/
MAP_IFRAME_LINK = "https://maps.google.com/maps?q=granada&t=&z=13&ie=UTF8&iwloc=&output=embed"

# https://cookie-bar.eu/
COOKIES_SCRIPT = "https://cdn.jsdelivr.net/npm/cookie-bar/cookiebar-latest.min.js?forceLang=es&theme=altblack&tracking=1&thirdparty=1&always=1&refreshPage=1&showNoConsent=1"

EVENT_KEYNOTERS = [
    {
        "name": 'John Smith',
        "photo_big": 'https://bulma.io/images/placeholders/1280x960.png',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    },
    {
        "name": 'John Smith',
        "photo_big": 'https://bulma.io/images/placeholders/1280x960.png',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    },
    {
        "name": 'John Smith',
        "photo_big": 'https://bulma.io/images/placeholders/1280x960.png',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    },
    {
        "name": 'John Smith',
        "photo_big": 'https://bulma.io/images/placeholders/1280x960.png',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    },
]

SPONSORS = {
    "gold": [
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
    ],
    "silver": [
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
    ],
    "metal": [
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
    ],
}

EVENT_TRACKS = json.dumps([
     { "id": 'core', "title": 'Track Core' },
     { "id": 'data', "title": 'Track Data', "eventColor": 'green' },
     { "id": 'web', "title": 'Track Web', "eventColor": 'orange' },
])

EVENT_START_DATE = "2022-09-30"
EVENT_TALKS = json.dumps(
    [
        {
            "id":"1",
            "resourceId":"core",
            "start":"2022-09-30T15:00:00",
            "end":"2022-09-30T17:30:00",
            "title":"Introducción a Data Science en Python",
            "editable":False,
            "description":"Francisco Correoso, Guillem Duran, Juan Carlos González, Jordi Contestí, Antònia Tugores",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"2",
            "resourceId":"web",
            "start":"2022-09-30T15:00:00",
            "end":"2022-09-30T17:30:00",
            "title":"TDD de cero a cien (o casi)",
            "editable":False,
            "description":"TDD de cero a cien (o casi)",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"3",
            "resourceId":"data",
            "start":"2022-09-30T15:00:00",
            "end":"2022-09-30T17:30:00",
            "title":"Representación de datos geográficos",
            "editable":False,
            "description":"Representación de datos geográficos",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"4",
            "resourceId": "data",
            "start":"2022-09-30T17:30:00",
            "end":"2022-09-30T18:00:00",
            "title":"Café",
            "editable":False,
            "description":"Café",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"5",
            "resourceId": "web",
            "start":"2022-09-30T17:30:00",
            "end":"2022-09-30T18:00:00",
            "title":"Café",
            "editable":False,
            "description":"Café",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"6",
            "resourceId": "core",
            "start":"2022-09-30T17:30:00",
            "end":"2022-09-30T18:00:00",
            "title":"Charla con un título bastante largo",
            "editable":False,
            "description":"Café",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"7",
            "resourceId": "data",
            "start":"2022-09-30T18:00:00",
            "end":"2022-09-30T20:30:00",
            "title":"¡Eureka! - Python y ciencia",
            "editable":False,
            "description":"¡Eureka! - Python y ciencia",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"8",
            "resourceId": "web",
            "start":"2022-09-30T18:00:00",
            "end":"2022-09-30T20:30:00",
            "title":"Las herramientas de un detective",
            "editable":False,
            "description":"Las herramientas de un detective",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"9",
            "resourceId": "core",
            "start":"2022-09-30T18:00:00",
            "end":"2022-09-30T20:30:00",
            "title":"Pyomo – Optimización en Python",
            "editable":False,
            "description":"Pyomo – Optimización en Python",
            "url":"https://stackoverflow.com/"
        },

    ]
)
