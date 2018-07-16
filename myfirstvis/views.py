from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import pymysql
from pyecharts import Bar
from pyecharts import Page
from pyecharts import Pie

from pyecharts import WordCloud


def index(request):
    return render(request, 'myfirstvis/single1.html')


def charts(request):
    # template = loader.get_template('myfirstvis/pyecharts.html')
    template = loader.get_template('myfirstvis/render.html')
    context = {
        "myechart": bbb()
    }
    return HttpResponse(template.render(context, request))


def bbb():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["yif", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    bar.show_config()
    bar.render(r"templates/myfirstvis/render.html")


def search_post(request):
    if request.POST:
        te = request.POST['text']
        na = request.POST['name']
        print(te)
        print(na)
        ctx = []
        ctx1 = []
        ctx2 = []

        page = Page()

        # 选择为名称时
        if na == 'name':
            sql = '%s%s%s%s%s%s%s' % (
            "select name, rating_num from res5_utf8 where ", str(na), " like '%", str(te), "%' ",
            " order by rating_num DESC ", 'limit 10;')
            res = (my_Sql(sql).replace("(", "").replace(")", "").replace("'", ""))
            ctx = res.split(',')
            for i in range(0, len(ctx), 2):
                if ctx[i]:
                    ctx1.append(ctx[i])
            for n in range(1, len(ctx), 2):
                if ctx[n]:
                    ctx2.append(ctx[n])
            ba = bar("电影评分", ctx1, ctx2)
            page.add(ba)

        # 选择为导演时
        if na == 'director':

            # 使用柱状图
            sql_ba = '%s%s%s%s%s%s%s' % (
            "select name, rating_num from res5_utf8 where ", str(na), " like '%", str(te), "%' ",
            " order by rating_num DESC ", 'limit 10;')
            res_ba = (my_Sql(sql_ba).replace("(", "").replace(")", "").replace("'", ""))
            ctx_ba = res_ba.split(',')
            for i in range(0, len(ctx_ba), 2):
                if ctx_ba[i]:
                    ctx1.append(ctx_ba[i])
            for n in range(1, len(ctx_ba), 2):
                if ctx_ba[n]:
                    ctx2.append(ctx_ba[n])
            ba = bar("电影评分", ctx1, ctx2)
            page.add(ba)

            res_1 = genre_num('剧情', 'director', str(te))
            res_2 = genre_num('动作', 'director', str(te))
            res_3 = genre_num('科幻', 'director', str(te))
            res_4 = genre_num('悬疑', 'director', str(te))
            res_5 = genre_num('冒险', 'director', str(te))
            res_6 = genre_num('爱情', 'director', str(te))
            res_7 = genre_num('历史', 'director', str(te))
            res_8 = genre_num('喜剧', 'director', str(te))
            res_9 = genre_num('战争', 'director', str(te))
            res_10 = genre_num('奇幻', 'director', str(te))

            attr = ['剧情', '动作', '科幻', '悬疑', '冒险', '爱情', '历史', '喜剧', '战争', '奇幻']
            value = [res_1, res_2, res_3, res_4, res_5, res_6, res_7, res_8, res_9, res_10]

            pi = pie("影片类型占比", attr, value)

            page.add(pi)

        # 当选择为年份
        if na == 'year':
            # 使用柱状图
            sql_ba = '%s%s%s%s%s%s%s' % (
            "select name, rating_num from res5_utf8 where ", str(na), " like '%", str(te), "%' ",
            " order by rating_num DESC ", 'limit 15;')
            res_ba = (my_Sql(sql_ba).replace("(", "").replace(")", "").replace("'", ""))
            ctx_ba = res_ba.split(',')
            for i in range(0, len(ctx_ba), 2):
                if ctx_ba[i]:
                    ctx1.append(ctx_ba[i])
            for n in range(1, len(ctx_ba), 2):
                if ctx_ba[n]:
                    ctx2.append(ctx_ba[n])
            ba = bar("电影评分", ctx1, ctx2)
            page.add(ba)

            # 使用饼图
            res_year_1 = genre_num('剧情', 'year', str(te))
            res_year_2 = genre_num('动作', 'year', str(te))
            res_year_3 = genre_num('科幻', 'year', str(te))
            res_year_4 = genre_num('悬疑', 'year', str(te))
            res_year_5 = genre_num('冒险', 'year', str(te))
            res_year_6 = genre_num('爱情', 'year', str(te))
            res_year_7 = genre_num('历史', 'year', str(te))
            res_year_8 = genre_num('喜剧', 'year', str(te))
            res_year_9 = genre_num('战争', 'year', str(te))
            res_year_10 = genre_num('奇幻', 'year', str(te))

            attr_year = ['剧情', '动作', '科幻', '悬疑', '冒险', '爱情', '历史', '喜剧', '战争', '奇幻']
            value_year = [res_year_1, res_year_2, res_year_3, res_year_4, res_year_5, res_year_6, res_year_7,
                          res_year_8, res_year_9, res_year_10]
            pi_year = pie("年份影片类型占比", attr_year, value_year)
            page.add(pi_year)

        if na == "genre":
            # 使用柱状图
            sql_ba = '%s%s%s%s%s%s%s' % (
                "select name, rating_num from res5_utf8 where ", str(na), " like '%", str(te), "%' ",
                " order by rating_num DESC ", 'limit 15;')
            res_ba = (my_Sql(sql_ba).replace("(", "").replace(")", "").replace("'", ""))
            ctx_ba = res_ba.split(',')
            for i in range(0, len(ctx_ba), 2):
                if ctx_ba[i]:
                    ctx1.append(ctx_ba[i])
            for n in range(1, len(ctx_ba), 2):
                if ctx_ba[n]:
                    ctx2.append(ctx_ba[n])
            ba = bar("电影评分", ctx1, ctx2)
            page.add(ba)

            # 使用词云图
            res_genre1 = genre_sum("剧情")
            res_genre2 = genre_sum("动作")
            res_genre3 = genre_sum("科幻")
            res_genre4 = genre_sum("悬疑")
            res_genre5 = genre_sum("冒险")
            res_genre6 = genre_sum("爱情")
            res_genre7 = genre_sum("历史")
            res_genre8 = genre_sum("喜剧")
            res_genre9 = genre_sum("战争")
            res_genre10 = genre_sum("奇幻")

            attr_genre = ['剧情', '动作', '科幻', '悬疑', '冒险', '爱情', '历史', '喜剧', '战争', '奇幻']
            value_genre = [res_genre1, res_genre2, res_genre3, res_genre4, res_genre5, res_genre6, res_genre7,
                           res_genre8, res_genre9, res_genre10]

            wcloud = wordcloud(attr_genre, value_genre)

            page.add(wcloud)

        if na == "actor":
            # 使用柱状图
            sql_ba = '%s%s%s%s%s%s%s' % (
                "select name, rating_num from res5_utf8 where ", str(na), " like '%", str(te), "%' ",
                " order by rating_num DESC ", 'limit 15;')
            res_ba = (my_Sql(sql_ba).replace("(", "").replace(")", "").replace("'", ""))
            ctx_ba = res_ba.split(',')
            for i in range(0, len(ctx_ba), 2):
                if ctx_ba[i]:
                    ctx1.append(ctx_ba[i])
            for n in range(1, len(ctx_ba), 2):
                if ctx_ba[n]:
                    ctx2.append(ctx_ba[n])
            ba = bar("电影评分", ctx1, ctx2)
            page.add(ba)

            # 使用饼图
            res_actor_1 = genre_num('剧情', 'actor', str(te))
            res_actor_2 = genre_num('动作', 'actor', str(te))
            res_actor_3 = genre_num('科幻', 'actor', str(te))
            res_actor_4 = genre_num('悬疑', 'actor', str(te))
            res_actor_5 = genre_num('冒险', 'actor', str(te))
            res_actor_6 = genre_num('爱情', 'actor', str(te))
            res_actor_7 = genre_num('历史', 'actor', str(te))
            res_actor_8 = genre_num('喜剧', 'actor', str(te))
            res_actor_9 = genre_num('战争', 'actor', str(te))
            res_actor_10 = genre_num('奇幻', 'actor', str(te))

            attr_actor = ['剧情', '动作', '科幻', '悬疑', '冒险', '爱情', '历史', '喜剧', '战争', '奇幻']
            value_actor = [res_actor_1, res_actor_2, res_actor_3, res_actor_4, res_actor_5, res_actor_6, res_actor_7,
                           res_actor_8, res_actor_9, res_actor_10]

            pi_actor = pie("参演电影类型占比", attr_actor, value_actor)
            page.add(pi_actor)

        page.render(r"templates/myfirstvis/render.html")
        return render(request, 'myfirstvis/render.html')


# 柱状图
def bar(name, ctx1, ctx2):
    ba = Bar("评分排行", width=1200, height=600)
    ba.add(str(name), ctx1, ctx2)
    return ba


# 饼图
def pie(title, ctx1, ctx2):
    pi = Pie(str(title), width=1200, height=600)
    pi.add(" ", ctx1, ctx2, is_label_show=True)
    return pi


# 词云图
def wordcloud(ctx1, ctx2):
    wc = WordCloud("类型占比", width=1200, height=600)
    wc.add("", ctx1, ctx2, word_size_range=[40, 200], shape='diamond')
    return wc


# 返回类型的总数
def genre_num(arg, ty, name):
    sql = '%s%s%s%s%s%s%s%s%s%s' % (
        "select count(*) from res5_utf8 where genre like ", "'%", str(arg), "%'", " and ", str(ty), " like ", "'%",
        str(name), "%' ")
    res = (my_Sql(sql).replace("(", "").replace(")", "").replace("'", "")).replace(",", "")

    return res


# 返回不同类型电影的总数
def genre_sum(arg):
    sql = '%s%s%s%s' % ("select count(*) from res5_utf8 where genre like ", "'%", str(arg), "%'")
    res = (my_Sql(sql).replace("(", "").replace(")", "").replace("'", "")).replace(",", "")
    return res


def my_Sql(statement):
    # 连接数据库
    db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='movie',
                         charset='utf8')
    # 设置一个游标
    cursor = db.cursor()
    # 执行SQL语句
    cursor.execute(statement)
    # 获得返回结果
    data = cursor.fetchall()
    return str(data)



