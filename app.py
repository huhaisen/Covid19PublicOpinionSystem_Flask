from flask import Flask
from flask import render_template
from flask import jsonify
import utils
import getDatas

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/time')
def getTime():
    return utils.get_time()

@app.route('/queryHotTopicList')
def queryHotTopicList():
    indicators = []
    positiveValues = []
    negativeValues = []
    data = getDatas.queryHotTopicList()
    for item in data:
        indicators.append({"name": item[0], "max": 1})
        positiveValues.append(item[1])
        negativeValues.append(item[2])
    return jsonify({"indicators": indicators, "positiveValues": positiveValues, "negativeValues": negativeValues})

@app.route('/queryStaGender')
def queryStaGender():
    datas = getDatas.querStaGender()
    data = datas[0]
    print(data)
    return jsonify({"maleNum": data[0], "femaleNum": data[1]})

@app.route('/queryStaProvinceDistribute')
def queryStaProvinceDistribute():
    data = getDatas.queryStaProvinceDistribute()
    dataLists = []
    for item in data:
        dataLists.append({
            "name": item[0],
            "value": item[1]
        })
    return jsonify({"dataLists": dataLists})

@app.route('/queryStaWordFrequency')
def queryStaWordFrequency():
    data = getDatas.queryStaWordFrequency()
    dataLists = []
    for item in data:
        dataLists.append({
            "name": item[0],
            "value": item[1]
        })
    return jsonify({"dataLists": dataLists})

@app.route('/queryTopWords')
def queryTopWords():
    data = getDatas.queryTopWords()
    wordNameList = []
    wordNumList = []
    for item in data:
        wordNameList.append(item[0])
        wordNumList.append(item[1])
    wordNumList.reverse()
    wordNameList.reverse()
    return jsonify({"wordNameList": wordNameList, "wordNumList": wordNumList})

@app.route('/queryStaNetizenAttention')
def queryStaNetizenAttention():
    data = getDatas.queryStaNetizenAttention()
    stanaDateList = []
    attentionNumList = []
    for item in data:
        stanaDateList.append(item[1].strftime('%m-%d'))
        attentionNumList.append(item[0])
    return jsonify({"stanaDateList": stanaDateList, "attentionNumList": attentionNumList})

@app.route('/queryTopProvinceDistribute')
def queryTopProvinceDistribute():
    data = getDatas.queryTopProvinceDistribute()
    provinceNameList = []
    sentimentNumList = []
    for item in data:
        provinceNameList.append(item[0])
        sentimentNumList.append(item[1])
    return jsonify({"provinceNameList": provinceNameList, "sentimentNumList": sentimentNumList } )



if __name__ == '__main__':
    app.run()
