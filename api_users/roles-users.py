
VISTA_SUPER={'super_admin':'vista_super'}

VISTA_SECTOR_ADMIN = {
    'cecasit':[
        {'admin': 'vista_crear_cecasit_worker'},
        {'rio_negro':'rio_negro_view'},
        {'chaco':'chaco_view'}
    ],
    'bajada':[
        {'admin': 'vista_crear_cecasit_worker'},
        {'txt':'txt_view'},
        {'imagenes':'imagenes_view'}
    ]
}

VISTA_WORKER = {
    'cecasit':[
            {'rio_negro':'rio_negro_view'},
            {'chaco':'chaco_view'}
        ],
    'bajada':[
            {'txt':'txt_view'},
            {'imagenes':'imagenes_view'}
        ]
}

import pprint
pprint.pprint(VISTA_SECTOR_ADMIN['cecasit'])




usuario={
    'usuario':'tom',
    'passw':'123456',
    'info':{
        'nombre':'Tomas',
        'apellido': 'Gomez Wagner',
        'email':'twagner@cecaitra.org.ar'
    },
    'rol':{
        'type':'sector_admin',
        'sector':'cecasit',
    }
}

rol = usuario['rol']['type']
sector = usuario['rol']['sector']

if rol == 'super_admin':
    print('super admin')
elif rol == 'sector_admin':
    print(f'{rol=}')
    print(VISTA_SECTOR_ADMIN[sector])
elif rol == 'worker':
    print('worker')


