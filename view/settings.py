from frame_txt import FrameFiltratTxt
from frame_img import FrameFiltratImg


VISTA_SUPER={'super_admin':'vista_super'}

VISTA_SECTOR_ADMIN = {
    # 'cecasit':[
        # {'admin': 'vista_crear_cecasit_worker'},
        # {'rio_negro':'rio_negro_view'},
        # {'chaco':'chaco_view'}
    # ],
    'bajada':[
        {'admin': 'vista_crear_cecasit_worker'},
        {'txt':'txt_view'},
        {'imagenes':'imagenes_view'}
    ]
}

VISTA_WORKER = {
    'cecasit':[
            {'filtrar_txt':FrameFiltratTxt},
            # {'rio_negro':'rio_negro_view'},
            # {'chaco':'chaco_view'}
        ],
    'bajada':[
            {'filtrar_txt':FrameFiltratTxt},
            {'filtrar_img':FrameFiltratImg},
        ]
}

VISTAS = {'super_admin':VISTA_SUPER, 'sector_admin':VISTA_SECTOR_ADMIN, 'worker':VISTA_WORKER}


