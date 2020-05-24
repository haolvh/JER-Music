import json
import threading
from urllib.parse import quote
import pymysql
import requests
import time

'''
*******************************************************QQ音乐************************************************************
'''


class QQMusic:
    def __init__(self, name):
        self.name = name

    def get_mid(self):
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt' \
              '.yqq.song&searchid=57951070373539875&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%s' \
              '&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json' \
              '&needNewCode=0' % quote(
            self.name)
        headers = {
            'Referer': 'https://y.qq.com/portal/search.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.181 Safari/537.36 '
        }
        response = json.loads(requests.get(url=url, headers=headers).content.decode('utf-8'))['data']['song']['list']
        # print(response)
        # response1 = json.loads(requests.get(url=url, headers=headers).content.decode('utf-8'))['data']['song']['time']
        # print(response1)
        return [x['mid'] for x in response], list(
            map(lambda x: [time.strftime('%M:%S', time.gmtime(x['interval'])), ''.join(x['title'].split()),
                           ''.join(x['album']['pmid'].split()),
                           '/'.join([i['name'] for i in x['singer']])], response))

    def sprider(self):
        songmids, informations = self.get_mid()
        # print(songmids)
        # print(informations)
        newinfro = []
        for songmid, information in zip(songmids, informations):
            data = '%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A' \
                   '%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%224776407682%22%2C%22calltype%22%3A0%2C' \
                   '%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C' \
                   '%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%224776407682%22%2C%22songmid%22' \
                   '%3A%5B%22' + songmid + '%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22' \
                                           '%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C' \
                                           '%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D '
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey23927290711706184&g_tk=5381&loginUin=0' \
                  '&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0' \
                  '&data=%s' % data
            headers = {
                'Referer': 'https://y.qq.com/portal/player.html',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/65.0.3325.181 Safari/537.36 '
            }
            response = json.loads(requests.get(url=url, headers=headers).content.decode('utf-8'))['req_0']['data']
            if response['midurlinfo'][0]['purl'] != '':
                URL = response['sip'][0] + response['midurlinfo'][0]['purl']
                information.append(URL)
                newinfro.append(information)
            else:
                information.append('-' * 180)
                # informations.remove(information)
                # print(information)
        # print(newinfro)
        return newinfro


def start(name):
    a = QQMusic(name)
    # print('>>开始爬取QQ音乐')
    a_ = a.sprider()
    # print(a_)
    for i in a_:
        # print(i[0] + " " + i[1] + " " + "https://y.gtimg.cn/music/photo_new/T002R300x300M000" + i[2] + ".jpg" + " " + i[
        #     3] + " " + i[4])
        mysql_initial(i[0], i[1], "https://y.gtimg.cn/music/photo_new/T002R300x300M000" + i[2] + ".jpg", i[3], i[4])
    print("初始化完成！")


def update(name):
    a = QQMusic(name)
    # print('>>开始爬取QQ音乐')
    a_ = a.sprider()
    # print(a_)
    for i in a_:
        # print(i[0] + " " + i[1] + " " + "https://y.gtimg.cn/music/photo_new/T002R300x300M000" + i[2] + ".jpg" + " " + i[
        #     3] + " " + i[4])
        mysql_update(i[0], i[1], "https://y.gtimg.cn/music/photo_new/T002R300x300M000" + i[2] + ".jpg", i[3], i[4])
    print("更新完成！")


class down_mysql:
    def __init__(self, music_time, music_name, music_pic, music_singer, music_url):
        self.music_time = music_time
        self.music_pic = music_pic
        self.music_singer = music_singer
        self.music_name = music_name
        self.music_url = music_url
        self.connect = pymysql.connect(
            host='localhost',
            db='music',
            port=3306,
            user='root',
            passwd='lv2016.',
            charset='utf8',
            use_unicode=False
        )
        self.cursor = self.connect.cursor()

    def save_mysql(self):
        sql = "insert into jermusic_musicintro(`music_name`,`music_URL`,`music_singer`,`music_time`, `music_pic`) VALUES (%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql,
                                (self.music_name, self.music_url, self.music_singer, self.music_time, self.music_pic))
            self.connect.commit()
            # print("success")
        except:
            self.connect.rollback()
            # print("fail")

    def update_mysql(self):
        sql = "update jermusic_musicintro set music_URL = '%s'  where music_name='%s' and music_singer='%s'" % (
            self.music_url, self.music_name, self.music_singer)
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # print("success")
        except:
            self.connect.rollback()
            # print("fail")


def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


def mysql_initial(music_time, music_name, music_pic, music_singer, music_url):
    down = down_mysql(music_time, music_name, music_pic, music_singer, music_url)
    down.save_mysql()


def mysql_update(music_time, music_name, music_pic, music_singer, music_url):
    down = down_mysql(music_time, music_name, music_pic, music_singer, music_url)
    down.update_mysql()


def update1():
    ff = open("MusicSource/singer.txt", encoding="utf8")
    for line in ff:
        print(line.strip())
        update(line.strip())
    print(time.time())
    threading.Timer(5*3600, update1).start()


def music_source():
    f = open("MusicSource/singer.txt", encoding="utf8")
    for line in f:
        # print(line.strip())
        start(line.strip())

    update1()
