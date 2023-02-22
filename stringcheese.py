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


def feature_support(__pattern__, __string__, group=0):
    temp_str = re.compile(__pattern__).search(__string__)
    if temp_str is None:
        temp_str = 'X'
    else:
        temp_str = 'O'
    return temp_str


def hotcheese_cpu(purestr):
    p_name = recompiler_exception('^.+(?= \\(.+\\).+ 스펙)', purestr)
    p_socket = recompiler_exception('소켓.{3,4}(?=\\))', purestr)
    p_core = recompiler_exception('(?<= / )[0-9+]{1,8}(?=코어)', purestr)
    p_thread = recompiler_exception('(?<= / ).{1,6}(?=쓰레드)', purestr)
    p_base_clk = recompiler_exception('(?<=기본 클럭: )[0-9.]+(?=GHz)', purestr)
    p_boost_clk = recompiler_exception('(?<=최대 클럭: )[0-9.]+(?=GHz)', purestr)
    p_l2c = recompiler_exception('(?<=L2 캐시: )[0-9.]{1,5}(?=MB)', purestr)
    p_l3c = recompiler_exception('(?<=L3 캐시: )[0-9.]{1,5}(?=MB)', purestr)
    p_tdp = recompiler_exception('(?<=TDP: ).{1,10}(?=W)|(?<=PBP/MTP: ).{1,10}(?=W)', purestr)
    p_pcie = recompiler_exception('PCIe[0-9., ]+(?= / )', purestr)
    p_mem0 = recompiler_exception('(?<=메모리 규격: )[a-zA-Z0-9, ]+(?= / )', purestr)
    p_mem1 = recompiler_exception('[0-9]{4}MHz|[0-9]{4}, [0-9]{4}(?=MHz)', purestr)
    p_d_gpu = recompiler_exception('(?<=내장그래픽: ).{2,3}(?= / )', purestr)
    if p_d_gpu == "탑재":
        p_d_gpu = re.compile('(?<=내장그래픽: 탑재 / ).{1,15}(?= / )|(?<=내장그래픽: 탑재 / ).{1,15}(?= 등록월)') \
            .search(purestr).group()
    p_bundle_cooler = recompiler_exception('(?<=쿨러: ).{1,20}(?= / )|(?<=쿨러: ).{1,20}(?=등록월)|(?<=쿨러: ).{1,20}(?= 등록월)',
                                           purestr, '미기재')
    p_price_retail = recompiler_exception('(?<=[0-9]몰상품비교)[0-9,]+원(?=가격정보 더보기정품)', purestr)
    p_price_bulk = recompiler_exception('(?<=[0-9]몰상품비교)[0-9,]+원(?=가격정보 더보기벌크)', purestr)
    p_price_multi = recompiler_exception('(?<=[0-9]몰상품비교)[0-9,]+원(?=가격정보 더보기멀티팩\\(정품\\))', purestr)
    item = [p_name, p_price_retail, p_price_bulk, p_price_multi,
            p_core, p_thread, p_base_clk, p_boost_clk, p_l3c, p_d_gpu, p_mem1, p_tdp, p_socket, p_bundle_cooler]
    string = ''
    for i in item:
        string = string + i + '\t'
    return string


def hotcheese_mb(purestr):
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
    item = [p_name, p_price, p_formfactor, p_mem0, p_mem1, p_mem2,
            p_hdmi, p_dp, p_sata, p_m2, p_vrm, p_drmos, p_rgb, p_lan_audio]
    string = ''
    for i in item:
        string = string + i + '\t'
    return string


def hotcheese_ram(purestr):
    p_name = recompiler_exception('(^.+(?=상세 스펙)).+ / ([DR45]+) / ([0-9]{1,5}MHz)', purestr, 'X', 1)
    p_type = recompiler_exception('(^.+(?=상세 스펙)).+ / ([DR45]+) / ([0-9]{1,5}MHz)', purestr, 'X', 2)
    p_clk = recompiler_exception('(^.+(?=상세 스펙)).+ / ([DR45]+) / ([0-9]{1,5}MHz)', purestr, 'X', 3)
    p_timing = recompiler_exception('(?<=램타이밍: )[CL0-9-]+(?= / )', purestr)
    p_voltage = recompiler_exception('(?<= / )\d\.\d\d[vV]', purestr)
    p_led = recompiler_exception('(?<=LED색상: ).{,10}(?= / |등록월)', purestr)
    p_heatsink = recompiler_exception('(?<=히트싱크: )방열판', purestr)
    p_heatsink_color = ''
    if p_heatsink == '방열판':
        p_heatsink = 'O'
        p_heatsink_color = recompiler_exception('(?<=방열판 색상: ).{,7}(?= / |등록월)', purestr)
    else:
        p_heatsink_color = 'X'
    price_pattern = '(?<=몰상품비교)((([0-9,]{,10}원)가격정보 더보기|일시품절|가격비교예정)(\d{,2}GB\([0-9Gx]{,5}\)|\d{,3}GB))'
    price_group = re.compile(price_pattern).findall(purestr)
    price_yum = ''
    for i in price_group:
        if i[1] == '가격비교예정' or i[1] == '일시품절':
            price_yum = price_yum + str(i[3] + '\t' + i[1]) + '\t'
        else:
            price_yum = price_yum + str(i[3] + '\t' + i[2]) + '\t'
    item = [p_name, p_clk, p_timing, p_voltage, p_heatsink, p_heatsink_color, p_led, price_yum]
    string = ''
    for i in item:
        string = string + i + '\t'
    return string


def hotcheese_vga(purestr):
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
    item = [name, price, base_clk, boost_clk, fan, plen, slot, power, tdp, psu, core]
    string = ''
    for i in item:
        string = string + i + '\t'
    return string


def hotcheese_ssd(purestr):
    name = recompiler_exception('(^.+(?=상세 스펙))', purestr)
    price_pattern = '(?<=몰상품비교)((([0-9,]{,10}원)가격정보 더보기|일시품절|가격비교예정)([0-9.,]{,5}TB|[0-9.,]{,5}GB))'
    price_group = re.compile(price_pattern).findall(purestr)
    price_yum = ''
    for i in price_group:
        if i[1] == '가격비교예정' or i[1] == '일시품절':
            price_yum = price_yum + str(i[3] + '\t' + i[1]) + '\t'
        else:
            price_yum = price_yum + str(i[3] + '\t' + i[2]) + '\t'
    price = price_yum
    formfactor = recompiler_exception('(?<=상세 스펙내장형SSD / ).{,13}(?= / )', purestr)
    phy = recompiler_exception('SATA\d|PCIe\d\.0x\d', purestr)
    protocol = recompiler_exception('(?<= / )(NVMe [a-z0-9.]{1,4}|NVMe)(?= / )', purestr)
    dram = recompiler_exception('DDR.+?(?= / )', purestr)
    nand_3d = recompiler_exception('3D낸드', purestr)
    nand_cell = recompiler_exception('(?<= / )(SLC|MLC|TLC|QLC)(?=\()', purestr)
    if nand_3d == '3D낸드':
        nand_cell = '3D ' + nand_cell
    controller = recompiler_exception('(?<= / 컨트롤러: ).+?(?= / )', purestr)
    io_r = recompiler_exception('((?<=순차읽기: )[0-9,]+?(?=MB))|((?<=순차읽기: 최대 )[0-9,]+?(?=MB))', purestr)
    io_w = recompiler_exception('(?<=순차쓰기: )[0-9,]+?(?=MB)', purestr)
    trim = feature_support('TRIM', purestr)
    gc = feature_support('GC', purestr)
    smart_info = feature_support('S\.M\.A\.R\.T', purestr)
    ecc = feature_support('ECC', purestr)
    devslp = feature_support('DEVSLP', purestr)
    slc_cache = feature_support('SLC.[캐시싱]{,2}', purestr)
    warranty = recompiler_exception('(?<=A/S기간: )\d(?=년)', purestr)  # year
    item = [name, formfactor, phy, protocol, nand_cell, controller, io_r, io_w,
            trim, gc, smart_info, ecc, devslp, slc_cache, warranty, price]
    string = ''
    for i in item:
        string = string + i + '\t'
    return string


def hotchesse_hdd(purestr):
    name = recompiler_exception('^.+?(?=/)', purestr)
    type = recompiler_exception('HDD\s\((.+?)\)', purestr, 'X', 1)
    formfactor = recompiler_exception('[0-9\.]+?(?=인치)', purestr)
    protocol = recompiler_exception('SATA[2-3]|SA-SCSI\s\(12Gb/s\)', purestr)
    if protocol == 'SA-SCSI (12Gb/s)':
        protocol = 'SAS 12G'
    buffer_cache = recompiler_exception('(?<=메모리 ).+?(?=MB)', purestr)
    brrrrrrt = recompiler_exception('(?<= / )[\d,]+?(?=RPM)', purestr)
    price = ''
    price_pattern = '(?<=상품비교)(.+?원)가격정보 더보기(.+?[BGT]{2})'
    price_group = re.compile(price_pattern).findall(purestr)
    for i in price_group:
        price = price + str(i[1] + '\t' + i[0] + '\t')
    item = [name, type, formfactor, protocol, buffer_cache, brrrrrrt, price]
    string = ''
    for i in item:
        string = string + i + '\t'
    return string
