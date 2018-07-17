# -*- coding: utf-8 -*-

import re


def replace(input):

    output = input

    output = re.sub(u'\u1000', u'\u0075', output)#kagyi
    output = re.sub(u'\u1001', u'\u0063', output)#kha_kway
    output = output.replace(u'\u1002', u'\u002a')#ga_nge
    output = re.sub(u'\u1003', u'\u0043', output)#ga_gyi
    output = re.sub(u'\u1004', u'\u0069', output)#nga
    output = re.sub(u'\u1005', u'\u0070', output)#sa_lone
    output = re.sub(u'\u1006', u'\u0071', output)#sa_lane
    output = re.sub(u'\u1007', u'\u005A', output)#za_gwe
    output = re.sub(u'\u1009', u'\u00DA', output)#nya_pyat
    output = re.sub(u'\u100A', u'[\u006E\u00F1', output)#nya
    output = re.sub(u'\u100B', u'\u0023', output)#ta_talin_gait
    output = re.sub(u'\u100E', u'\u0058', output)#hta_wen_bae
    output = re.sub(u'\u100D', u'\u0021', output)#da_yin_gout
    output = re.sub(u'\u100E', u'\u00A1', output)#da_yin_mote
    output = re.sub(u'\u100F', u'\u0050', output)#na_gyi
    output = re.sub(u'\u1010', u'\u0077', output)#ta_wen_pu
    output = re.sub(u'\u1011', u'\u0078', output)#ta_sin_tuu
    output = re.sub(u'\u1012', u'\u0027', output)#da_dway
    output = re.sub(u'\u1013', u'\u0022', output)#da_oat_chait
    output = re.sub(u'\u1014', u'[\u0045\u0065', output)#na_nge
    output = re.sub(u'\u1015', u'\u0079', output)#pa_sout
    output = re.sub(u'\u1016', u'\u007A', output)#pa_oo_htoke
    output = re.sub(u'\u1017', u'\u0041', output)#ba_dad_chait
    output = re.sub(u'\u1018', u'\u0062', output)#ba_gone
    output = re.sub(u'\u1019', u'\u0072', output)#ma
    output = re.sub(u'\u101A', u'\u002C', output)#ya_ba_lat
    output = re.sub(u'\u101B', u'[\u0026\u00BD]', output)#ya_gout
    output = re.sub(u'\u101C', u'\u0076', output)#la
    output = re.sub(u'\u101D', u'\u0030', output)#wa
    output = re.sub(u'\u101E', u'\u006F', output)#ta
    output = re.sub(u'\u101F', u'\u005B', output)#ha
    output = re.sub(u'\u1020', u'\u0056', output)#la_gyi
    output = re.sub(u'\u1021', u'\u0074', output)#ar



    output = re.sub(u'\u1023', u'\u00A3', output)# 2kagyi
    output = re.sub(u'\u1024', u'\u00fe', output)# II
    output = re.sub(u'\u1025', u'[\u004f\u00cd]', output)# oo
    output = re.sub(u'\u1027', u'\u007b', output)# at_kayar_a
    output = re.sub(u'\u102b', u'\u0067', output)# yay_char_ashay
    output = re.sub(u'\u102c', u'\u006d', output)# yay_char
    output = re.sub(u'\u102d', u'\u0064', output)# longgyitin
    output = re.sub(u'\u102e', u'\u0044', output)# longgyitin_sanke
    output = re.sub(u'\u1026', u'\u1025\u102e', output)# oo with longyitinsanke
    output = re.sub(u'\u102f', u'[\u004b\u006b]', output)# 1_chuang_ngin
    output = re.sub(u'\u1030', u'[\u004c\u006c]', output)# 2_chuang_ngin
    output = re.sub(u'\u1031', u'\u0061', output)#ta_wai_htoe
    output = re.sub(u'\u1032', u'\u004a',  output)#naut_htoe_pyit
    output = re.sub(u'\u1036', u'\u0048',  output)#taytay_tin
    output = re.sub(u'\u1037', u'[\u0055\u0059\u0068]', output)# aut_myit
    output = re.sub(u'\u1038', u'\u003b', output)#wa_sa_paut
    output = re.sub(u'\u103a', u'\u0066', output)# nga_tat
    output = re.sub(u'\u103b', u'[\u0073\u00df]', output)# ya_pint
    output = re.sub(u'\u1008', u'\u1005\u103b', output)  # za_myit_zwe
    output = re.sub(u'\u103c', u'[\u006A\u0042\u004d\u004e\u0060\u007e]', output)# ya_yit
    output = re.sub(u'\u103d', u'\u0047', output)#wa_swe
    output = re.sub(u'\u103e', u'[\u0053\u00a7]', output)# ha_toe
    output = re.sub(u'\u1003f', u'\u00f3', output)#ta_gyi


    ###
    # nunbers
    output = re.sub(u'\u1041', u'\u0031', output)  # one
    output = re.sub(u'\u1042', u'\u0032', output)  # two
    output = re.sub(u'\u1043', u'\u0033', output)  # three
    output = re.sub(u'\u1044', u'\u0034', output)  # four
    output = re.sub(u'\u1045', u'\u0035', output)  # five
    output = re.sub(u'\u1046', u'\u0036', output)  # six
    output = re.sub(u'\u1047', u'\u0037', output)  # seven
    output = re.sub(u'\u1048', u'\u0038', output)  # eight
    output = re.sub(u'\u1049', u'\u0039', output)  # nine
    # output = re.sub(u'([\u1041-\u1049])\u101d', u'\\1\u1040', output)  # zero

    output = output.replace(u'\u104a', u'\u003f')  # pot_kalay
    output = output.replace(u'\u104b', u'\u002f')  # pot_ma
    output = re.sub(u'\u104c', u'\u00fc', output)  # nai
    output = re.sub(u'\u104d', u'\u00ed', output)  # yway
    output = re.sub(u'\u104e', u'\u00a4', output)  # la_guang
    output = output.replace(u'\u104f', u'\u005c')  # ii
    output = output.replace(u'[', u'\u00ab')
    output = output.replace(u']', u'\u00bb')

    return output

def decompose(input):
    output = input

    output = re.sub(u'\u102b\u103a', u'\u003a', output)  # yaychar_shayhtoe
    output = output.replace(u'\u1000\u103b\u1015\u103a', u'\u0024')  # kyat_sign
    output = re.sub(u'\u103c\u103d', u'[\u003c\u003e]', output)  # yayit_waswe
    output = re.sub(u'\u100f\u1039\u100d', u'\u0040', output)  # nagyi_sint_tawenbae
    output = re.sub(u'\u103e\u102f', u'\u0049',  output)  # hatoe_1chaungngin
    output = re.sub(u'\u103b\u102f', u'[\u0051\u00fb]', output)  # yapint_1cn
    output = re.sub(u'\u103b\u103d', u'\u0052',  output)  # yapint_waswe
    output = re.sub(u'\u103d\u103e', u'\u0054',  output)  # waswe_hatoe
    output = re.sub(u'\u103b\u103d\u103e', u'\u0057',  output)  # yapint_waswe_hatoe
    output = output.replace(u'\u100b\u1039\u100c', u'\u007c')  # ttlg_with_twb
    output = re.sub(u'\u103e\u1030', u'\u00aa',  output)  # hatoe_2cn

    # pr_sint
    output = re.sub(u'\u1039\u1003', u'\u00a2',  output)  # ga_gyi
    output = re.sub(u'\u100b\u1039\u100b', u'\u00a5', output)  # twice_ttlg
    output = re.sub(u'\u1039\u1011', u'\u00a6', output)  # hta_sin_htoo
    output = re.sub(u'\u1039\u1013', u'\u00a8', output)  # da_aut_chai
    output = re.sub(u'\u1039\u1001', u'\u00a9',  output)  # ka_kwe
    output = re.sub(u'\u1039\u1018', u'[\u00ac\u00c7]', output)  # ba_gone
    output = re.sub(u'\u1039\u1019', u'\u00ae',  output)  # ma
    output = re.sub(u'\u1039\u100c', u'\u00b2', output)  # ta_wen_bae
    output = re.sub(u'\u1039\u100b', u'\u00b3', output)  # ta_ta_lin_gyake
    output = re.sub(u'\u1039\u1012', u'\u00b4', output)  # da_dway
    output = re.sub(u'\u100d\u1039\u100e', u'\u00b9', output)  # da_yin_mout_with_da_yin_gaut
    output = re.sub(u'\u1039\u1002', u'\u00be', output)  # ga_nge
    output = re.sub(u'\u1039\u1017', u'\u00c1', output)  # ba_lat_chai
    output = re.sub(u'\u1039\u1010', u'[\u00c5\u00e5]', output)  # da_wen_bu
    output = re.sub(u'\u1039\u1007', u'\u00c6', output)  # za_gwe
    output = re.sub(u'\u1039\u1010\u103d', u'\u00c9', output)  # twa
    output = re.sub(u'\u1039\u1008', u'\u00d1', output)  # za_myin_zwe
    output = re.sub(u'\u1009\u102c', u'\u00d3', output)  # nya_with_yaychar
    output = re.sub(u'\u1039\u100f', u'\u00d6', output)  # na_gyi
    output = re.sub(u'\u100d\u1039\u100d', u'\u00d7', output)  # twice_dyg
    output = re.sub(u'\u1039\u1015', u'\u00dc', output)  # pa_saut
    output = re.sub(u'\u1039\u1006', u'\u00e4', output)  # sa_lane
    output = re.sub(u'\u1039\u1016', u'\u00e6', output)  # pa_oo_htoke
    output = re.sub(u'\u1039\u1014', u'\u00e9',  output)  # na_nge
    output = re.sub(u'\u1039\u1005', u'\u00f6', output)  # sa_lone
    output = re.sub(u'\u1039\u1000', u'\u00fa', output)  # ka_gyi
    output = re.sub(u'\u1039\u101c', u'\u2019', output)  # la

    # nga_sint
    output = re.sub(u'([\u1000-\u1021])\u0046', u'\u0046', output)  # normal
    output = re.sub(u'([\u1000-\u1021])\u00d0', u'\u0046\u102e', output)  # with_longyitin_sanke
    output = re.sub(u'([\u1000-\u1021])\u00d8', u'\u0046\u102d', output)  # with_longyitin
    output = re.sub(u'([\u1000-\u1021])\u00f8', u'\u0046\u1036', output)  # with_taytaytin
    output = re.sub(u'\u1004\u103a\u1039', u'\u0046', output)
    output = re.sub(u'\u102d\u1036', u'\u00f0', output)

    return output

def visual2logical(input):
    # reorder the sequence of characters from visual to logical
    output = input
    # 1=tawaetoe
    # 2=yayit
    # 3=letter
    # 4=yapint
    # 5=waswe
    # 6=hatoe
    # 7=aumyit
    # 8=yaychar
    output = re.sub(u'((?:\u1031)?)((?:\u103c)?)([\u1000-\u1021])((?:\u103b)?)((?:\u103d)?)((?:\u103e)?)((?:\u1037)?)((?:\u102c)?)', '\\3\\2\\4\\5\\6\\1\\7\\8', output)

    return output


def convert(input):

    output = replace(input)
    output = decompose(input)
    output = visual2logical(output)

    return output





