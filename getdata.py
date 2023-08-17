from roboflow import Roboflow
rf = Roboflow(api_key="B4ihF6wSXUuKFODabDe3")
project = rf.workspace("roboflow-gw7yv").project("fish-yzfml")
dataset = project.version(44).download("yolov8")
