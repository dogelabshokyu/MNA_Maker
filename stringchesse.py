# making crawled data to json type first and editing as MNA style
import re


def tabsonic(*args):
    text = ''
    for i in args:
        text += i + "\t"
    return text


def recompiler_exception(keyword, keyfrom, whenexcept='X', group=0):
    rce_tmp = re.compile(keyword).search(keyfrom)
    if rce_tmp is None:
        rce_tmp = whenexcept
    else:
        rce_tmp = rce_tmp.group(group)
    return rce_tmp


json_data = {}


def string_JSON_cpu(purestr):
    p_name = recompiler_exception('^.+(?= \\(.+\\).+ 스펙)', purestr, 'X')
    p_socket = recompiler_exception('소켓.{3,4}(?=\\))', purestr, 'X')
    p_core = recompiler_exception('(?<= / )[0-9+]{1,8}(?=코어)', purestr, 'X')
    p_thread = recompiler_exception('(?<= / ).{1,6}(?=쓰레드)', purestr, 'X')
    p_base_clk = recompiler_exception('(?<=기본 클럭: )[0-9.]+(?=GHz)', purestr, 'X')
    p_boost_clk = recompiler_exception('(?<=최대 클럭: )[0-9.]+(?=GHz)', purestr, 'X')
    p_tdp = recompiler_exception('(?<=TDP: ).{1,10}(?=W)|(?<=PBP/MTP: ).{1,10}(?=W)', purestr, 'X')
    p_pcie = recompiler_exception('PCIe[0-9., ]+(?= / )', purestr, 'X')
    p_mem0 = recompiler_exception('(?<=메모리 규격: )[a-zA-Z0-9, ]+(?= / )', purestr, 'X')
    p_mem1 = recompiler_exception('[0-9]{4}MHz|[0-9]{4}, [0-9]{4}(?=MHz)', purestr, 'X')
    p_d_gpu = recompiler_exception('(?<=내장그래픽: ).{2,3}(?= / )', purestr, 'X')
    if p_d_gpu == "탑재":
        p_d_gpu = re.compile('(?<=내장그래픽: 탑재 / ).{1,15}(?= / )|(?<=내장그래픽: 탑재 / ).{1,15}(?= 등록월)') \
            .search(purestr).group()
    p_bundle_cooler = recompiler_exception('(?<=쿨러: ).{1,20}(?= / )|(?<=쿨러: ).{1,20}(?=등록월)|(?<=쿨러: ).{1,20}(?= 등록월)',
                                           purestr, '미기재')
    p_price_retail = recompiler_exception('(?<=[0-9]몰상품비교)[0-9,]+원(?=가격정보 더보기정품)', purestr, 'X')
    p_price_bulk = recompiler_exception('(?<=[0-9]몰상품비교)[0-9,]+원(?=가격정보 더보기벌크)', purestr, 'X')
    p_price_multi = recompiler_exception('(?<=[0-9]몰상품비교)[0-9,]+원(?=가격정보 더보기멀티팩\\(정품\\))', purestr, 'X')
    jdata = \
        {
            'p_name': p_name,
            'p_socket': p_socket,
            'p_core': p_core,
            'p_thread': p_thread,
            'p_base_clk': p_base_clk,
            'p_boost_clk': p_boost_clk,
            'p_l3': 'x',
            'p_tdp': p_tdp,
            'p_pcie': p_pcie,
            'p_mem0': p_mem0,
            'p_mem1': p_mem1,
            'p_d_gpu': p_d_gpu,
            'p_bundle_cooler': p_bundle_cooler,
            'p_price_retail': p_price_retail,
            'p_price_multi': p_price_multi,
            'p_price_bulk': p_price_bulk
        }
    return jdata


def cooking_cpu(ijk):
    item = ['p_name', 'p_price_retail', 'p_price_bulk', 'p_price_multi',
            'p_core', 'p_thread', 'p_base_clk', 'p_boost_clk', 'p_l3', 'p_d_gpu', 'p_mem1', 'p_tdp',
            'p_socket', 'p_bundle_cooler']
    string = ''
    for i in item:
        string = string + ijk[i] + '\t'
    return string


def stringJSON_MB(purestr):
    p_name = recompiler_exception('^.+(?=상세 스펙인텔|상세 스펙AMD)', purestr)
    p_price = recompiler_exception('(?<=상품비교)[0-9,]{1,10}원(?=가격정보 더보기)', purestr, '일시품절')
    p_socket = recompiler_exception('(?<=상세 스펙).{1,12}(?= / )', purestr)
    p_pch = recompiler_exception('((?<=상세 스펙).{1,15}(?<= / ))(AMD |인텔 )([a-zA-Z][0-9]{3}(?= / ))', purestr, 'X', 3)
    p_formfactor = recompiler_exception('(AMD |인텔 )([a-zA-Z0-9]{3,5}(?= / )) / (.*(?<=cm\)))', purestr, 'X', 3)
    # 5000MHz (PC4-40000) <- 90% PC4-25600 (3,200MHz) <- 10%
    p_mem0 = recompiler_exception('((?<= / 메모리 )[DR45]{4}(?= / )) / ([0-9]{4}(?=MHz)).* / (\d)개 / ', purestr, 'X', 1)
    p_mem1 = recompiler_exception('((?<= / 메모리 )[DR45]{4}(?= / )) / ([0-9]{4}(?=MHz)).* / (\d)개 / ', purestr, 'X', 2)
    p_mem2 = recompiler_exception('((?<= / 메모리 )[DR45]{4}(?= / )) / ([0-9]{4}(?=MHz)).* / (\d)개 / ', purestr, 'X', 3)
    if p_mem0 == 'X':
        p_mem0 = recompiler_exception('((?<= / 메모리 )[DR45]{4}(?= / )) / (\d)개 / ', purestr, 'X', 1)
        p_mem1 = 'X'
        p_mem2 = recompiler_exception('((?<= / 메모리 )[DR45]{4}(?= / )) / (\d)개 / ', purestr, 'X', 2)
    p_hdmi = recompiler_exception('(?<= / )HDMI(?= / )', purestr)
    if p_hdmi == 'X':
        p_hdmi = 'X'
    else:
        p_hdmi = 'O'
    p_dp = recompiler_exception('(?<= / )DP(?= / )', purestr)
    if p_dp == 'X':
        p_dp = 'X'
    else:
        p_dp = 'O'
    p_sata = recompiler_exception('(?<=SATA3: )[0-9](?=개 / )', purestr)
    p_m2 = recompiler_exception('(?<=M\.2: )[0-9](?=개 / )', purestr)
    p_lan_audio = recompiler_exception('(?=랜/오디오).+(?= / 내부I/O)', purestr)
    if p_lan_audio == 'X':
        p_lan_audio = recompiler_exception('(?=오디오잭).+(?= / 내부I/O)', purestr)
    p_vrm = recompiler_exception('(?<=전원부: ).+(?=페이즈)', purestr)
    p_drmos = recompiler_exception('Dr\.MOS', purestr)
    if p_drmos == 'X':
        p_drmos = 'X'
    else:
        p_drmos = 'O'
    p_rgb = recompiler_exception('RGB 헤더', purestr)
    if p_rgb == 'X':
        p_rgb = 'X'
    else:
        p_rgb = 'O'
    abc = \
        {
            'p_name': p_name, 'p_price': p_price, 'p_formfactor': p_formfactor,
            'p_mem0': p_mem0, 'p_mem1': p_mem1, 'p_mem2': p_mem2, 'p_hdmi': p_hdmi, 'p_dp': p_dp,
            'p_sata': p_sata, 'p_m2': p_m2, 'p_lan_audio': p_lan_audio,
            'p_vrm': p_vrm, 'p_drmos': p_drmos, 'p_rgb': p_rgb
        }
    return abc


def cooking_mb(qwer):
    item = ['p_name', 'p_price', 'p_formfactor', 'p_mem0', 'p_mem1', 'p_mem2', 'p_hdmi', 'p_dp',
            'p_sata', 'p_m2', 'p_vrm', 'p_drmos', 'p_rgb', 'p_lan_audio']
    string = ''
    for i in item:
        string = string + qwer[i] + '\t'
    return string


def hotchesse_ram(purestr):
    p_name = recompiler_exception('(^.+(?=상세 스펙)).+ / ([DR45]+) / ([0-9]{1,5}MHz)', purestr, 'X', 1)
    p_type = recompiler_exception('(^.+(?=상세 스펙)).+ / ([DR45]+) / ([0-9]{1,5}MHz)', purestr, 'X', 2)
    p_clk = recompiler_exception('(^.+(?=상세 스펙)).+ / ([DR45]+) / ([0-9]{1,5}MHz)', purestr, 'X', 3)
    p_timing = recompiler_exception('(?<=램타이밍: )[CL0-9-]+(?= / )', purestr)
    p_voltage = recompiler_exception('(?<= / )\d\.\d\d[vV]', purestr)
    p_led = recompiler_exception('(?<=LED색상: ).{,10}(?= / |등록월)', purestr)
    p_heatsink = recompiler_exception('(?<=히트싱크: )방열판', purestr, 'X')
    p_heatsink_color = ''
    if p_heatsink == '방열판':
        p_heatsink = 'O'
        p_heatsink_color = recompiler_exception('(?<=방열판 색상: ).{,7}(?= / |등록월)', purestr)
    else:
        p_heatsink_color = 'X'
    price_patteren = '(?<=몰상품비교)((([0-9,]{,10}원)가격정보 더보기|일시품절|가격비교예정)(\d{,2}GB\([0-9Gx]{,5}\)|\d{,3}GB))'
    price_group = re.compile(price_patteren).findall(purestr)
    price_yum = ''
    for i in price_group:
        if i[1] == '가격비교예정' or i[1] == '일시품절':
            price_yum = price_yum + str(i[3]+'\t'+i[1]) + '\t'
        else:
            price_yum = price_yum + str(i[3]+'\t' + i[2]) + '\t'
    item = [p_name, p_clk, p_timing, p_voltage, p_heatsink, p_heatsink_color, p_led, price_yum]
    string = ''
    for i in item:
        string = string + i + '\t'
    return string


def stringjson_vga(purestr):
    name = recompiler_exception('(^.+(?=상세 스펙))', purestr)
    price = recompiler_exception('(?<=상품비교)[0-9,]{1,10}원(?=가격정보 더보기)', purestr, '일시품절')
    base_clk = recompiler_exception('(?<=베이스클럭: ).{1,5}(?=MHz)', purestr)
    boost_clk = recompiler_exception('(?<=부스트클럭: ).{1,5}(?=MHz)', purestr)
    fan = recompiler_exception('(?<= / ).(?=개 팬)', purestr)
    plen = recompiler_exception('(?<=가로\(길이\): ).{,7}(?=mm)', purestr)
    slot = recompiler_exception('(?<=높이\(두께\): ).{,7}(?=mm)', purestr)
    power = recompiler_exception('(?<=전원 포트: ).{,9}핀 x.개(?= / )', purestr)
    tdp = recompiler_exception('(?<=사용전력: 최대 )[0-9]+W(?= / )|(?<=사용전력: 최대)[0-9]+W(?= / )', purestr)
    psu = recompiler_exception('(?<=정격파워 )[0-9]+W(?= 이상)', purestr)
    core = recompiler_exception('(?<=스트림 프로세서: )[0-9]+(?=개 / )', purestr)
    abc = \
        {
            'name': name, 'price': price, 'base_clk': base_clk, 'boost_clk': boost_clk,
            'fan': fan, 'plen': plen, 'slot': slot, 'power': power, 'tdp': tdp, 'psu': psu, 'core': core
        }
    return abc


def cooking_vga(qwer):
    item = ['name', 'price', 'base_clk', 'boost_clk', 'fan', 'plen', 'slot', 'power', 'tdp', 'psu', 'core']
    string = ''
    for i in item:
        string = string + qwer[i] + '\t'
    return string
