from deepface import DeepFace
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
result = DeepFace.verify("./card.png", "./photo.png", model_name = models[6])
print(str(result))