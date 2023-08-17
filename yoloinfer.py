from ultralytics import YOLO

model = YOLO('runs/detect/train6/weights/best.pt')
results = model.predict(source='fish.jpg',show=False,save=True)

for result in results:
    boxes = result.boxes
    print(boxes)

print(results[0].xywh)
print(results[0].cls)

#수정
