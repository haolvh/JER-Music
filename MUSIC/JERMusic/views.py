import json
import traceback

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from JERMusic.models import Clist, MusicIntro, User
from MusicSource.MusicGet import music_source

music_source()


# 用户收藏业务处理
def collect(request):
    # 接受前端POST请求数据
    # 将request中的接送数据提取出来
    info = json.loads(request.body)
    try:
        user_name = info['username']
        music_name = info['music_name']
        # print(user_name)
        # print(music_name)
    except Exception as e:

        result = {"ret": -1, "msg": "请传入完整参数！" + str(e)}
        return JsonResponse(result)

    # 判断参数是否不存在或为空值
    if user_name is not None and user_name != '' \
            and \
            music_name is not None and music_name != '':
        # 参数不为空 去数据库找记录
        # 如果当前记录存在 则不插入 给前端返回相应信息
        # 如果当前记录不在  则插入该条记录
        try:
            data = Clist.objects.values().filter(music_name=music_name, user_name=user_name)
            if (list(data).__len__()) > 0:
                result = {"ret": -1, "msg": "该歌曲已收藏！"}
            else:
                song = list(MusicIntro.objects.values('music_name', 'music_time', 'music_singer') \
                            .filter(music_name=music_name))
                # print(song)
                if song.__len__() > 0:
                    record = Clist.objects.create(
                        user_name=user_name,
                        music_name=music_name,
                        singer=song[0]['music_singer'],
                        time=song[0]['music_time'],
                    )
                    if record:
                        result = {"ret": 0, "data": song}
                    else:
                        result = {"ret": -1, "msg": "插入数据失败!"}
                else:
                    result = {"ret": -1, "msg": "歌曲信息不存在！"}
        except Exception as e:
            print(str(e))
            traceback.print_exc()
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            result = {"ret": -1, "msg": "插入异常！"}
    else:
        result = {"ret": -1, "msg": "请正确输入参数!"}
    return JsonResponse(result)


# 用户收藏展示业务处理
def show_collection(request):
    # 检查url是否有参数
    ph = request.GET.get("user_name", None)
    # 如果有，则添加过滤条件
    try:
        song_list = Clist.objects.values()
        data = list(song_list)
        result = {"ret": 0, "total": data.__len__(), "col_song": data}
    except Exception as e:
        result = {"ret": -1, "msg": "获取信息失败" + str(e)}
    return JsonResponse(result)


# 歌曲首页业务处理
def show_song(request):
    # 首页分页查询
    # 接受GET请求
    page = request.GET.get('page', default=1)
    page_size = int(request.GET.get('pageSize', default=8))
    result = {}

    song_list = MusicIntro.objects.values('music_name', 'music_URL', 'music_singer', 'music_pic', 'music_time')
    paginator = Paginator(song_list, page_size)
    result['total'] = paginator.count
    try:
        songs = paginator.page(page)
    except PageNotAnInteger:
        songs = paginator.page(1)
    except EmptyPage:
        songs = paginator.page(paginator.num_pages)
    result['data'] = list(songs)
    return JsonResponse(result)


# 搜索业务处理
def search(request):
    keyword = request.GET.get('keyword', None)

    if keyword is not None and keyword != '':
        try:
            song = MusicIntro.objects.values('music_name', 'music_URL', 'music_singer', 'music_time') \
                .filter(Q(music_name__contains=keyword) | Q(music_singer__contains=keyword))
            # print(song)
            # data['music_url'] = data.pop('music_URL')
            data = list(song)
            if data.__len__() > 0:
                result = {"ret": 0, "data": data}
            else:
                result = {"ret": -1, "msg": "歌曲不存在！请联系管理员添加"}
        except MusicIntro.DoesNotExist:
            result = {"ret": -1, "msg": "歌曲不存在！请联系管理员添加"}
    else:
        result = {"ret": -1, "msg": "没有keyword参数!"}

    return JsonResponse(result)


# 用户登录业务处理
def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    # print(username)
    # print(password)

    if username is not None and username != '' \
            and \
            password is not None and password != '':
        try:
            user = User.objects.get(user_name=username)
            data = model_to_dict(user)
            # print(data['user_name'])
            # print(data['user_password'])
            if data['user_name'] == username and data['user_password'] == password:
                result = {"ret": 0}
            else:
                result = {"ret": -1, "msg": "用户名或密码错误"}
        except User.DoesNotExist:
            result = {"ret": -1, "msg": "该用户不存在请先注册!"}
    else:
        result = {"ret": -1, "msg": "请正确输入用户名和密码"}

    return JsonResponse(result)


# 用户注册业务处理
def register(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    confirm_password = request.POST.get('confirm_password', None)
    tel = request.POST.get('tel', None)

    if username is None or username == '' \
            or password is None or password == '' \
            or confirm_password is None or confirm_password == '' \
            or tel is None or tel == '':
        result = {"ret": -1, "msg": "请正确输入注册信息"}
    elif password != confirm_password:
        # print(password)
        # print(confirm_password is not confirm_password)
        result = {"ret": -1, "msg": "密码确认有误"}
    else:
        try:
            if User.objects.get(user_name=username):
                result = {"ret": -1, "msg": "该用户已被注册"}
        except User.DoesNotExist:
            try:
                User.objects.create(user_name=username, user_password=password, user_tel=tel)
                result = {"ret": 0}
            except User.MultipleObjectsReturned:
                result = {"ret": 0, "msg": "用户添加失败"}

    return JsonResponse(result)


# 歌曲播放业务处理
def play(request):
    # 获取前端传过来的id
    music_id = request.GET.get('music_id', None)

    if music_id:
        try:
            song = MusicIntro.objects.get(music_id=music_id)
            data = model_to_dict(song)
            data.pop('music_id')
            data['music_url'] = data.pop('music_URL')
            result = {"ret": 0, "data": data}
        except MusicIntro.DoesNotExist:
            result = {"ret": -1, "msg": "歌曲不存在！请联系管理员添加"}
    else:
        result = {"ret": -1, "msg": "没有music_id参数!"}

    return JsonResponse(result)


# 歌曲下载业务处理
def download(request):
    # 获取前端传过来的id
    music_id = request.GET.get('music_id', None)

    if music_id:
        try:
            song = MusicIntro.objects.get(music_id=music_id)
            data = model_to_dict(song)
            data.pop('music_id')
            data.pop('music_name')
            data.pop('music_singer')
            data.pop('music_time')
            data.pop('music_pic')
            result = {"ret": 0, "music_url": data['music_URL']}
        except MusicIntro.DoesNotExist:
            result = {"ret": -1, "msg": "歌曲不存在！请联系管理员添加"}
    else:
        result = {"ret": -1, "msg": "没有music_id参数!"}

    return JsonResponse(result)
