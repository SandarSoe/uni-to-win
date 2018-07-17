# -*- coding: utf-8 -*-

import re


def convert(input):

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
    output = re.sub(u'\u102e', u'\u0044', output)  # longgyitin_sanke
    output = re.sub(u'\u1026', u'\u1025\u102e', output)  # oo with longyitinsanke
    output = re.sub(u'\u102f', u'[\u004b\u006b]', output)  # 1_chuang_ngin
    output = re.sub(u'\u1030', u'[\u004c\u006c]', output)  # 2_chuang_ngin
    output = re.sub(u'\u1031', u'\u0061', output)  # ta_wai_htoe
    output = re.sub(u'\u1032', u'\u004a',  output)  # naut_htoe_pyit
    output = re.sub(u'\u1036', u'\u0048',  output)  # taytay_tin
    output = re.sub(u'\u1037', u'[\u0055\u0059\u0068]', output)  # aut_myit
    output = re.sub(u'\u1038', u'\u003b', output)  # wa_sa_paut
    output = re.sub(u'\u103a', u'\u0066', output)  # nga_tat
    output = re.sub(u'\u103b', u'[\u0073\u00df]', output)  # ya_pint
    output = re.sub(u'\u1008', u'\u1005\u103b', output)  # za_myit_zwe
    output = re.sub(u'\u103c', u'[\u006A\u0042\u004d\u004e\u0060\u007e]', output)  # ya_yit
    output = re.sub(u'\u103d', u'\u0047', output)  # wa_swe
    output = re.sub(u'\u103e', u'[\u0053\u00a7]', output)  # ha_toe
    output = re.sub(u'\u1003f', u'\u00f3', output)  # ta_gyi

    return output
