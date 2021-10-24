from flask import Flask, render_template, request
from deepface import DeepFace

app = Flask(__name__)


@app.route('/', methods=['GET'])  # 全部API测试
def api_test():
    return render_template('app.html')


@app.route('/card', methods=['POST'])  # 上传身份证
def card():
    file = request.files['file']
    file.save("./card.png")
    return "上传身份证成功"


@app.route('/photo', methods=['POST'])  # 上传照片
def photo():
    file = request.files['file']
    file.save("./photo.png")
    return "上传身份证成功"


@app.route('/check', methods=['GET'])  # 检测
def check():
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
    try:
        result = DeepFace.verify("./card.png", "./photo.png", model_name = models[0])
        return str(result)
    except:
        return "error"