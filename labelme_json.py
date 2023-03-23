import json


class labelme_json:
    def __init__(self, shapes, imagePath, imageHeight, imageWidth, filename):
        self.imagePath = imagePath
        self.imageHeight = imageHeight
        self.imageWidth = imageWidth
        self.filename = filename
        self.shapes = []

        self.get_shapes(shapes)

    def write_to_file(self, path):
        label_json = {
            "version": "4.5.7",
            "flags": {},
            "shapes": self.shapes,
            "imagePath": self.imagePath,
            "imageData": None,
            "imageHeight": self.imageHeight,
            "imageWidth": self.imageWidth
            }
        # print(label_json)
        with open(path, 'w') as f:
            json.dump(label_json, f, indent=4, ensure_ascii=False)

    def get_shapes(self, shapes):
        for shape in shapes:
            d = {
               "label": shape.label,
               "points": shape.points,
               "group_id": None,
               "shape_type": shape.shape_type,
               "flags": {}
                }
            self.shapes.append(d)


class shape:
    def __init__(self, label, points, shape_type):
        self.label = label
        self.points = points
        self.shape_type = "polygon"
