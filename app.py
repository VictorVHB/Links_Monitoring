""" 
Urussanga
network 177.74.78.0 255.255.255.0 route-policy MEUS_ANUNCIOS(2019+2303+3012+50111)
network 177.74.76.0 255.255.255.0 route-policy MEUS_ANUNCIOS(2019+2201+2303+3012+50111)

Orleans
network 177.74.65.0 255.255.255.0 route-policy MEUS_ANUNCIOS(2019+2309+3059+50111)

São Ludgero
network 177.74.75.0 255.255.255.0 route-policy MEUS_ANUNCIOS(2019+2303+3053+50111)

Sap
network 138.117.194.0 255.255.255.0 route-policy MEUS_ANUNCIOS(2019+2303+3013+2203+50111) - CGNAT - 1

Minas
network 177.124.51.0 255.255.255.0 route-policy MEUS_ANUNCIOS(2019+2201+2303+3411+50111)
network 177.124.50.0 255.255.255.0 route-policy MEUS_ANUNCIOS(2019+2303+3011+50111)
network 177.124.48.0 255.255.255.0 route-policy MEUS_ANUNCIOS(2019+2303+3411+2203+50111) 

# Minas
route-policy MEUS_ANUNCIOS(2019+2203+3011+3411+50111) permit node 10
 apply ip-address next-hop 177.124.49.212
 apply local-preference 1050
 apply community 65316:1 65316:1000 65316:10000 65316:2019 65316:2203 65316:3011 65316:3411 53062:50111
#
 
#SAP
route-policy MEUS_ANUNCIOS(2019+2203+3011+50111) permit node 10
 apply ip-address next-hop 172.28.0.109
 apply local-preference 1050
 apply community 65316:9 65316:1000 65316:10000 65316:2019 65316:2203 65316:3011 53062:50111

# SL
route-policy MEUS_ANUNCIOS(2019+2203+2303+3053+50111) permit node 10
 apply ip-address next-hop 172.18.0.142
 apply local-preference 1050
 apply community 65316:2 65316:1000 65316:10000 65316:2019 65316:2203 65316:2303 65316:3053 53062:50111
#
 
# Uru
route-policy MEUS_ANUNCIOS(2019+2193+2302+3012+50111) permit node 10
 apply ip-address next-hop 172.20.4.143
 apply local-preference 1050
 apply community 65316:3 65316:1000 65316:10000 65316:2019 65316:2193 65316:2302 65316:3012 53062:50111
#
 Orl

route-policy MEUS_ANUNCIOS(2019+2199+50111) permit node 10
 apply ip-address next-hop 172.23.5.134
 apply local-preference 1050
 apply community 65316:4 65316:1000 65316:10000 65316:2019 65316:2199 53062:50111
#
 
Lista de community’s

65316:219x - ALT(GEGENET)
65316:220x - Contato
65316:230x - OI  (vtal)
65316:201x - Ox
65316:301x - Ix-sp(PTTvia eletronet)
65316:341x - Ix-sp(PTT via commcorp)
65316:302x - Ix-sc(PTT-florianópolis)
65316:309x - Ix-rj(PTT-rio de janeiro)
65316:303x - Ix-rs(PTT-porto alegre)
65316:305x - Ix-pr(PTT-curitiba)

caches ateky 

65316:802x - google
65316:803x - fna
65316:804x - netflix

Comunidades diferenciadas:
65316:8042 - Cliente Netflix e Google 

1 - prepend 1x
2 - prepend 2x
3 - prepend 3x
9 - nao anuncia

Bloco 51 Minas
Antes MEUS_ANUNCIOS(2019+2193+3411+50111)
Agora MEUS_ANUNCIOS(2019+2202+2302+3411+50111)

"""

