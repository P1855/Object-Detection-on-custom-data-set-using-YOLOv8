import os
import shutil


"P:/python for ai, dev/pythonProject/python_project_on_object_detection_in_custom_dataset/download" == os.path.join('.', 'data_all')

"P:/python for ai, dev/pythonProject/python_project_on_object_detection_in_custom_dataset/download" == os.path.join('.', 'data')

for set_ in ['train', 'validation', 'test']:
    for dir_ in [os.path.join("P:/python for ai, dev/pythonProject/python_project_on_object_detection_in_custom_dataset/output", set_),
                 os.path.join("P:/python for ai, dev/pythonProject/python_project_on_object_detection_in_custom_dataset/output", set_, 'imgs'),
                 os.path.join("P:/python for ai, dev/pythonProject/python_project_on_object_detection_in_custom_dataset/output", set_, 'anns')]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.mkdir(dir_)

alpaca_id = '/m/0pcr'

train_bboxes_filename = os.path.join('.', 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('.', 'validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join('.', 'test-annotations-bbox.csv')


for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    set_ = ['train', 'validation', 'test'][j]
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in [alpaca_id]:
                if not os.path.exists(os.path.join("P:/python for ai, dev/pythonProject/python_project_on_object_detection_in_custom_dataset/output", set_, 'imgs', '{}.jpg'.format(id))):
                    shutil.copy(os.path.join("P:/python for ai, dev/pythonProject/python_project_on_object_detection_in_custom_dataset/download", '{}.jpg'.format(id)),
                                os.path.join("P:/python for ai, dev/pythonProject/python_project_on_object_detection_in_custom_dataset/output", set_, 'imgs', '{}.jpg'.format(id)))
                with open(os.path.join("P:/python for ai, dev/pythonProject/python_project_on_object_detection_in_custom_dataset/output", set_, 'anns', '{}.txt'.format(id)), 'a') as f_ann:
                    # class_id, xc, yx, w, h
                    x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                    xc = (x1 + x2) / 2
                    yc = (y1 + y2) / 2
                    w = x2 - x1
                    h = y2 - y1

                    f_ann.write('0 {} {} {} {}\n'.format(xc, yc, w, h))
                    f_ann.close()

            line = f.readline()
