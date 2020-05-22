from django.shortcuts import render
from django.http import JsonResponse
from collection.models import Clist

# Create your views here.


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
        info[user_name] is not ""
        and info[music_name] is not ""
        and info[songer] is not ""
        and info[time] is not ""
    ):
        record = Clist.objects.create(
            id=max_id + 1,
            user_name=info["user_name"],
            music_name=info["music_name"],
            songer=info[songer],
            time=info[time],
        )
        return JsonResponse({"ret": 0, "msg": "添加收藏歌曲成功"})
    else:
        return JsonResponse({"ret": -1, "msg": "歌曲信息缺失，添加失败"})
