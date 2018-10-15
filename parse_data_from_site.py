import urllib.parse
import urllib.request
import re, csv

url_s = ['https://www.otodom.pl/oferta/siemianowice-bytkow-3-pokojowe-ID3MBzq.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/funkcjonalne-m3-do-wlasnej-aranzacji-ID3MvEc.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/atrakcyjne-w-wysokim-standardzie-ID3NEkQ.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/mieszkanie-na-poddaszu-jedyne-w-siemianowicach-ID3E3xO.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/gotowe-mieszkanie-mozliwosc-negocjacji-ID3LuKQ.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/siemianowice-slaskie-centrum-ul-powstancow-ID3FJCv.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/klimatyczne-mieszkanie-w-poblizu-parku-slaskiego-ID3LtdO.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/klimatyczne-m4-2-balkony-w-okolicy-bytkowa-ID3NlQs.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/mieszkanie-144-m-siemianowice-slaskie-ID3Ne4o.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/3-pokoje-kamienica-siemianowice-sl-bezposrednio-ID3IVag.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/siemianowice-slaskie-centrym-ul-hutnicza-ID3DrHK.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/mieszkanie-w-siemianowicach-slaskich-niski-czynsz-ID3MXZa.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/kawalerka-32m-w-ok-ul-szkolnej-ID3M0E4.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/nowoczesne-3-pokoje-blisko-parku-ID3MHqv.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/piekne-nowoczesne-4-pokoje-73m-ID3MECg.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/mieszkanie-37-m-siemianowice-slaskie-ID3MiMM.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         'https://www.otodom.pl/oferta/atrakcyjne-mieszkanie-2-pok-z-ogrodkiem-i-garazem-ID3MkQ4.html?utm_source=refferals&utm_medium=traffic_exchange&utm_campaign=OLX_nieruchomosci_ad#xtor=SEC-18',
         ]

# "district_name":"Bytk

def get_disciption(data):
    return re.findall(r'<p>(.*?)</p>', data)


def get_info_from_data(data):
    # print(data)
    try:
        print(re.search(r'czynsz|Czynsz.+?[0-9]+', data))
        # start, stop = re.search(r'czynsz|Czynsz.+[0-9]+', data).span()
        # print(data[start - 10:stop + 100])


    except Exception as e:
        print(e)
        # print(re.search(r'.?Building_floors_num.{5}', data))
        # start, stop = re.search(r'"surface"', data).span()
        # print(data[start - 1000: stop+20])
        # print(get_disciption(data))


def get_features(data):
    feature_num = 5
    data = re.findall(r'"ad_price":[0-9]+|'
                      r'"surface":.[0-9]+.|'
                      r'"rooms":.[0-9]+.|'
                      r'.?Building_floors_num.:.[0-9]+|'
                      r'Czynsz.+?[0-9]+', data)
    feature_row_vector = []
    for feature in data[:feature_num]:
        # print(feature)
        feature_row_vector += [re.search(r'[0-9]+', feature).group()]
    return [feature_row_vector]

def get_url_data(url):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.12 (KHTML, like Gecko) Maxthon/3.0 Chrome/26.0.1410.43 Safari/535.12'
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return str(response.read())

def save_to_file(path, feature_row_vec):
    s = ''
    with open(path, 'a') as file:
        for feature in feature_row_vec:
            file.write(feature + ',')
            s += feature + ','
        else:
            file.write('\n')
            s += '\n'
    # print(s)
    return s

def write_to_csv(path, data):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        for feature in data:
            writer.writerow(feature)

def create_header(path, headers_names):
    with open(path, 'w+') as file:
        write = csv.writer(file, delimiter=';')
        write.writerow(headers_names)


def read_and_save_to_file(path, headers):
    l = []
    create_header(path,headers)
    for url in url_s:
        resp_Data = get_url_data(url)
        feature_row_vec = get_features(resp_Data)
        write_to_csv(path, feature_row_vec)
        l += [feature_row_vec]
    return l


def main():
    headers = ['cena', 'pow', 'liczba pokoi', 'pietro', 'czynsz']
    try:
        l = read_and_save_to_file(r'C:\Users\seb\Desktop\m2.csv', headers)
    except Exception as e:
        print(e)
    else:
        for i, row in enumerate(l):
            print(i, row)

print(main())

# d = [['20000','30','2','4','200']]
# print(save_to_file(r'C:\Users\seb\Desktop\m2.csv', d))
# print(write_to_csv(r'C:\Users\seb\Desktop\m2.csv', d))
# write_to_csv(r'C:\Users\seb\Desktop\m2.csv', r'C:\Users\seb\Desktop\mieszkanie.txt')
# for i, url in enumerate(url_s):
#     data = get_url_data(url)
#     print(i)
#     feature_vec = get_features(data)
#     save_to_file(r'C:\Users\seb\Desktop\mieszkanie.txt', feature_vec)

# data = get_url_data(url_s[0])
# feature_vec = get_features(data)

