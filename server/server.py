# -*- coding: utf-8 -*- #
from flask import Flask
from flask import render_template, request, Response
import json, time, os
import azure, re
import deal_lesson, deal_classroom, sift_withoutcv

app = Flask(__name__)
g = {
    "state": 0,
    "stateMachine": {
        0: {
            "transfer": {
                "饿": [1],
                "吃": [1],
                "地铁": [3],
                "公交": [4],
                "今天.*?课": [10],
                "上(.*?)课": [5],
                "自习": [8],
                "else": [0, "什么? 我不明白, 试试换个问题"]
            },
            "answer": "好的"
        },
        1: {
            "transfer": {
                "艺园": [2, "艺园"],
                "艺园二楼": [2, "艺园"],
                "农园": [2, "农园"],
                "农园三楼": [2, "农园"],
                "畅春园三楼": [2, "畅春园"],
                "畅春园": [2, "畅春园"],
                "else": [1, "什么? 我不明白, 试试换个说法"]
            },
            "answer": "可以使用现金结算的餐厅有学校西侧的艺园二楼、学校东部的农园三楼以及北大西门外的畅春园三楼, 请问您想去哪一个?"
        },
        # 2: { // 应该进入导航页
        # }
        3: {
            "transfer": {
                "好": [2, "北京大学东门站"],
                "需要": [2, "北京大学东门站"],
                "是的": [2, "北京大学东门站"],
                "不用了": [0],
                "else": [3, "什么? 我不明白, 试试换个说法"]
            },
            "answer": "北京大学东门有地铁站北京大学东门站, 需要为您导航吗?"
        },
        4: {
            "transfer": {
                "东南门": [2, "北京大学东南门"],
                "南门": [2, "北京大学南门"],
                "小西门": [2, "北京大学小西门"],
                "else": [4, "什么? 我不明白, 试试换个说法"]
            },
            "answer": "北京大学东南门、南门、小西门门口均有公交站, 请问您要去哪个门的公交站?",
        },
        # 5: {
        # },
        # 6: {
        # },
        # 7: {
        # }
        8: {
            "answer": "请问您想去哪栋教学楼上自习呢?"
        },
        10: {
            "answer": ""
        }
    }
}


@app.route('/query/<question>')
def query(question):
    state = g.get("state")
    if state == 6:
        teacher = question
        classObj = deal_lesson.get_one_lesson(g.get("classes"), teacher)
        g["state"] = 7
        info = classObj.get("place")
        places = deal_classroom.get_all_buildings() #todo
        for place in places:
            if info.find(place) != -1:
                g["place"] = place
        return json.dumps({
            "direction": "answer",
            "param": "您想上的课程在" + info.decode("utf8") + ", 需要为您导航吗?"
        }, ensure_ascii=False)
    if state == 7:
        g["state"] = 0
        return json.dumps({
            "direction": "navigate",
            "param": g.get("place")
        }, ensure_ascii=False)
    if state == 8:

        if question not in deal_classroom.get_all_buildings():
            g["state"] = 0
            return json.dumps({
                "direction": "answer",
                "param": "不存在这个教学楼哦"
            }, ensure_ascii=False)

        g["state"] = 9
        g["place"] = question
        rooms = deal_classroom.get_empty_rooms(question) #todo
        return json.dumps({
            "direction": "navigate",
            "param": "今天" + question + "空闲的教室有" + "、".join(rooms) + ", 需要为您导航吗"
        }, ensure_ascii=False)
    if state == 9:
        g["state"] = 0
        return json.dumps({
            "direction": "navigate",
            "param": g["place"]
        }, ensure_ascii=False)

    transfer = g.get("stateMachine")[state]["transfer"]
    for q, answer in transfer.items():
        m = re.search(q.decode("utf8"), question)
        if m != None:
            g["state"] = transfer[q][0]
            if len(transfer[q]) > 1:
                param = transfer[q][1]
            res = g.get("stateMachine").get(g.get("state"), {}).get("answer")
            if g.get("state") == 2:
                g["state"] = 0
                return json.dumps({
                    "direction": "navigate",
                    "param": param
                }, ensure_ascii=False)
            elif g.get("state") == 5:
                className = m.group(1)
                classes = deal_lesson.get_lessons(className)
                if classes.__len__() == 1:
                    g["state"] = 7
                    classObj = classes[0]
                    return json.dumps({
                        "direction": "answer",
                        "param": "您想上的课程在" + "、".join(classObj.get("place")) + ", 需要为您导航吗?"
                    }, ensure_ascii=False)
                elif classes.__len__() > 1:
                    g["state"] = 6
                    g["classes"] = classes
                    return json.dumps({
                        "direction": "answer",
                        "param": "您想上的课程有多个老师开设:" + "、".join(map(lambda x: x["teacher"], classes)) + ", 想要上哪个老师的课?"
                    }, ensure_ascii=False)
                else:
                    g["state"] = 0
                    return json.dumps({
                        "direction": "answer",
                        "param": "查不到您要上的课程耶"
                    }, ensure_ascii=False)
            elif g.get("state") == 10:
                g["state"] = 0
                classes = deal_lesson.get_lesson_list()
                if not classes:
                    return json.dumps({
                        "direction": "answer",
                        "param": "您今天没有课"
                    })
                res = []
                for k in classes:
                    res.append(k['name'])
                return json.dumps({
                    "direction": "answer",
                    "param": "您今天有" + "、".join(res).decode("utf8") + "等课程"
                })
            elif state == g["state"]:
                return json.dumps({
                    "direction": "answer",
                    "param": param
                }, ensure_ascii=False)
            else:
                return json.dumps({
                    "direction": "answer",
                    "param": res
                }, ensure_ascii=False)

    g["state"] = transfer["else"][0]
    if len(transfer):
        param = transfer["else"][1]
    res = g.get("stateMachine").get(g.get("state"), {}).get("answer")
    if g.get("state") == 2:
        g["state"] = 0
        return json.dumps({
            "direction": "navigate",
            "param": param
        }, ensure_ascii=False)
    elif state == g.get("state"):
        return json.dumps({
            "direction": "answer",
            "param": param
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "direction": "answer",
            "param": res
        }, ensure_ascii=False)



@app.route('/faceRecog', methods=["POST"])
def faceRecog():
    file = request.files["img"]
    if file.filename == '':
        r = {'status': -1, 'failReason': "文件没有成功上传"}
        return Response(response=json.dumps(r), mimetype="text/html")
    else:
        filename = str(time.time()) + file.filename
        path = os.path.join("./server/identity", filename)
        file.save(path)
        res = azure.get_user_info(path)

        return json.dumps(res, ensure_ascii=False)


@app.route('/sceneRecog')
def sceneRecog():
    file = request.files["img"]
    if file.filename == '':
        r = {'status': -1, 'failReason': "文件没有成功上传"}
        return Response(response=json.dumps(r), mimetype="text/html")
    else:
        # filename = str(time.time()) + file.filename
        # path = os.path.join("./server/scene", filename)
        # file.save(path)
        path = os.path.join("./server/scene", "20151225102523748.gif")
        res = sift_withoutcv.get_intros(path)
        print res
        return res


@app.route('/navigate')
def hello_world():
    return render_template('gdmap.html')


if __name__ == '__main__':
    app.run(debug=True)