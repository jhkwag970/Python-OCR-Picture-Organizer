from OCR import ImageLabel
from EntityAnnotation import Annotation
import os
import sys

path="resources/"
file_list = os.listdir(path)

ocr_inst = ImageLabel()
#Open up Client 
ocr_inst.open_client()

sys.stdout = open('output.txt', 'w')

#Label Processing
annotation_list=[]
for file in file_list:
    labels = ocr_inst.detect_labels(path+file)
    i=0
    for label in labels:
        annotation_info = Annotation(file, label.description,label.score)
        annotation_list.append(annotation_info)
        i+=1
        if(i==3):
            break

# # #Examples
# print(label)
# print("-----------------------------")
# print(type(label))
# print("-----------------------------")
# print(type(label[0]))
# print(label[0].description)
# print(label[0].score)
# print(label[0].topicality)


# my_list = [   
#     "aaaa",
#     {'mid': '/m/01yrx', 'description': 'Cat', 'score': 0.956459463, 'topicality': 0.956459463},
#     {'mid': '/m/0d4v4', 'description': 'Window', 'score': 0.938840091, 'topicality': 0.938840091},
#     {'mid': '/m/0307l', 'description': 'Felidae', 'score': 0.89566052, 'topicality': 0.89566052},
#     {'mid': '/m/01lrl', 'description': 'Carnivore', 'score': 0.885138333, 'topicality': 0.885138333},
#     {'mid': '/m/01k9lj', 'description': 'Jaw', 'score': 0.880326807, 'topicality': 0.880326807},
#     {'mid': '/m/0276krm', 'description': 'Fawn', 'score': 0.816135049, 'topicality': 0.816135049}
# ]

# print(my_list[0])





