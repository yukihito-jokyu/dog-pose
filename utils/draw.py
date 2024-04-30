import json
import os
import cv2


def keypoints_reshape(keypoints):
    keypoint_num = 0
    for i, keypoint in enumerate(keypoints):
        # if score[i] > 0.6:
        #     keypoint_num += 1
        #     keypoint.append(2)
        # else:
        #     keypoint[0] = 0
        #     keypoint[1] = 0
        #     keypoint.append(0)
        if keypoint[0] == 0 and keypoint[1] == 0:
            keypoint.append(0)
        else:
            keypoint_num += 1
            keypoint.append(2)
    return keypoints, keypoint_num


class Draw:
    def __init__(self):
        # jsonファイルのロード
        base_dir = './utils/jsonfile'
        key_info_json_path = os.path.join(base_dir, 'keypoints_info.json')
        key_color_json_path = os.path.join(base_dir, 'key_color.json')
        with open(key_info_json_path, 'r') as json_file:
            self.key_info_json = json.load(json_file)
        with open(key_color_json_path, 'r') as json_file:
            self.key_color_json = json.load(json_file)
        self.skeleton = self.key_info_json.get('skeleton')
        self.bbox_color = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 255)]

    def draw_keypoints(self, img, keypoints):
        pass_list = [13,14,15,17,18,19,22]
        point_radius = 5
        point_thickness = -1
        for i, keypoint in enumerate(keypoints):
            if (keypoint[2] != 0) and (i not in pass_list):
                x = int(keypoint[0])
                y = int(keypoint[1])
                point_color = tuple(self.key_color_json[i])
                cv2.circle(img, (x, y), point_radius, point_color, point_thickness)
        return img


    def draw_skeleton(self, img, keypoints, line_color=(0, 0, 255)):
        for skeleton in self.skeleton:
            start_point_index = skeleton[0]
            end_point_index = skeleton[1]
            start_point = keypoints[start_point_index]
            end_point = keypoints[end_point_index]
            if start_point[2] != 0 and end_point[2] != 0:
                s_p = (int(start_point[0]), int(start_point[1]))
                e_p = (int(end_point[0]), int(end_point[1]))
                # line_color = (0, 0, 255)  # 赤色 (BGR形式)
                line_thickness = 2
                # 画像上に線を描画
                cv2.line(img, s_p, e_p, line_color, line_thickness)
        return img
    
    def keypoints_reshape(self, keypoints):
        reshape_keypoints = []
        keypoint_list = []
        for keypoint in keypoints:
            keypoint_list.append(keypoint)
            if len(keypoint_list) == 3:
                reshape_keypoints.append(keypoint_list)
                keypoint_list = []
        return reshape_keypoints
    
    def draw_bbox(self, img, bbox):
        # for bbox in bboxs:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), self.bbox_color[0], thickness=2)
        # cv2.rectangle(img, (int(y1), int(x1)), (int(y2), int(x2)), self.bbox_color[1], thickness=2)
        # cv2.rectangle(img, (int(x1), int(y2)), (int(x2), int(y1)), self.bbox_color[2], thickness=2)
        # cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), self.bbox_color[3], thickness=2)
        return img
    

    def create_bbox(self, keypoints, width, height):
        # x横,y縦
        max_x = 0
        min_x = width
        max_y = 0
        min_y = height
        expansion = 0.2
        for keypoint in keypoints:
            x = keypoint[0]
            y = keypoint[1]
            if 0 != keypoint[2]:
                if max_x < x:
                    max_x = x
                if min_x > x:
                    min_x = x
                if max_y < y:
                    max_y = y
                if min_y > y:
                    min_y = y
        length_x = max_x - min_x
        length_y = max_y - min_y
        min_x = min_x - (length_x * expansion)
        max_x = max_x + (length_x * expansion)
        min_y = min_y - (length_y * expansion)
        max_y = max_y + (length_y * expansion)
        if min_x < 0:
            min_x = 0
        if max_x > width:
            max_x = width
        if min_y < 0:
            min_y = 0
        if max_y > height:
            max_y = height
        return [min_x, min_y, max_x, max_y]