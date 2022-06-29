from django.urls import path
import gamesaver.views as view


urlpatterns = [
    path('', view.gamesaver),
    path('t1_T/', view.t1_T),
    path('t1_J/', view.t1_J),
    path('t1_M/', view.t1_M),
    path('t1_A/', view.t1_A),
    path('t1_S/', view.t1_S),

    #dk
    path('dk/', view.dk),
    path('dk_T/', view.dk_T),
    path('dk_J/', view.dk_J),
    path('dk_M/', view.dk_M),
    path('dk_A/', view.dk_A),
    path('dk_S/', view.dk_S),
    
    #drx
    path('drx/', view.drx),
    path('drx_T/', view.drx_T),
    path('drx_J/', view.drx_J),
    path('drx_M/', view.drx_M),
    path('drx_A/', view.drx_A),
    path('drx_S/', view.drx_S),

    #gen
    path('gen/', view.gen),
    path('gen_T/', view.gen_T),
    path('gen_J/', view.gen_J),
    path('gen_M/', view.gen_M),
    path('gen_A/', view.gen_A),
    path('gen_S/', view.gen_S),

    #lsb
    path('lsb/', view.lsb),
    path('lsb_T/', view.lsb_T),
    path('lsb_J/', view.lsb_J),
    path('lsb_M/', view.lsb_M),
    path('lsb_A/', view.lsb_A),
    path('lsb_S/', view.lsb_S),

    #kdf
    path('kdf/', view.kdf),
    path('kdf_T/', view.kdf_T),
    path('kdf_J/', view.kdf_J),
    path('kdf_M/', view.kdf_M),
    path('kdf_A/', view.kdf_A),
    path('kdf_S/', view.kdf_S),

    #kt
    path('kt/', view.kt),
    path('kt_T/', view.kt_T),
    path('kt_J/', view.kt_J),
    path('kt_M/', view.kt_M),
    path('kt_A/', view.kt_A),
    path('kt_S/', view.kt_S),

    #hle
    path('hle/', view.hle),
    path('hle_T/', view.hle_T),
    path('hle_J/', view.hle_J),
    path('hle_M/', view.hle_M),
    path('hle_A/', view.hle_A),
    path('hle_S/', view.hle_S),

    #ns
    path('ns/', view.ns),
    path('ns_T/', view.ns_T),
    path('ns_J/', view.ns_J),
    path('ns_M/', view.ns_M),
    path('ns_A/', view.ns_A),
    path('ns_S/', view.ns_S),

    #bro
    path('bro/', view.bro),
    path('bro_T/', view.bro_T),
    path('bro_J/', view.bro_J),
    path('bro_M/', view.bro_M),
    path('bro_A/', view.bro_A),
    path('bro_S/', view.bro_S),
]