from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse

# Create your views here.
from JEmoudel.models import MusicIntro, User, Clist


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


def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    # print(username)
    # print(password)

    if username is not None and username is not '' \
            and \
            password is not None and password is not '':
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


def register(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    confirm_password = request.POST.get('confirm_password', None)
    tel = request.POST.get('tel', None)

    if username is None or username is '' \
            or password is None or password is '' \
            or confirm_password is None or confirm_password is '' \
            or tel is None or tel is '':
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


def search(request):
    search_msg = request.GET.get('search_msg', None)

    if search_msg is not None:
        try:
            song = MusicIntro.objects.values().filter(Q(music_name__contains=search_msg) | Q(music_singer__contains=search_msg))
            # print(song)
            # data = [{"adasd": "Asdas"}]
            # data['music_url'] = data.pop('music_URL')
            data = list(song)
            if data.__len__() > 0:
                result = {"ret": 0, "data": data}
            else:
                result = {"ret": -1, "msg": "歌曲不存在！请联系管理员添加"}
        except MusicIntro.DoesNotExist:
            result = {"ret": -1, "msg": "歌曲不存在！请联系管理员添加"}
    else:
        result = {"ret": -1, "msg": "没有search_msg参数!"}

    return JsonResponse(result)


def test(request):
    result = {"msg": "success!"}
    return JsonResponse(result)



def allcollection(request):
    # 检查url是否有参数
    ph = request.GET.get("user_name", None)
    # 如果有，则添加过滤条件
    try:
        song_list = Clist.objects.values()
        data = list(song_list)
        result = {"ret": 0, "total": data.__len__(), "col_song": data}
    except:
        result = {"ret": -1, "msg": "获取信息失败"}
    return JsonResponse(result)


def addSong(request):
    # 获取参数
    info = request.params["data"]
    # 获取数据库下一个id值
    listid = Clist.objects.values("id")
    max_id = max(list(listid))
    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    if (
        info['user_name'] is not ""
        and info['music_name'] is not ""
        and info['songer'] is not ""
        and info['time'] is not ""
    ):
        record = Clist.objects.create(
            id=max_id + 1,
            user_name=info["user_name"],
            music_name=info["music_name"],
            songer=info['songer'],
            time=info['time'],
        )
        return JsonResponse({"ret": 0, "msg": "添加收藏歌曲成功"})
    else:
        return JsonResponse({"ret": -1, "msg": "歌曲信息缺失，添加失败"})





