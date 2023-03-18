import sys
import numpy as np
import time

def tasks_sort(*workshops):
    task = []
    workshops = list(workshops)
    # workshops_sort_by_in = workshops.sort(key = lambda x:int(x.in_status), reverse=True)
    
    # workshops_sort_by_out = [workshop for workshop in workshops if workshop.out_status=='1']
    
    # if workshops_sort_by_out:
    #     workshops_sort_by_out.sort(key = lambda x: int(x.type), reverse=True)
    workshops_type9 = [workshop for workshop in workshops if workshop.type=='9']
    workshops_type8 = [workshop for workshop in workshops if workshop.type=='8']
    workshops_type7 = [workshop for workshop in workshops if workshop.type=='7']
    workshops_type6 = [workshop for workshop in workshops if workshop.type=='6']
    workshops_type5 = [workshop for workshop in workshops if workshop.type=='5']
    workshops_type4 = [workshop for workshop in workshops if workshop.type=='4']
    workshops_type3 = [workshop for workshop in workshops if workshop.type=='3']
    workshops_type2 = [workshop for workshop in workshops if workshop.type=='2']
    workshops_type1 = [workshop for workshop in workshops if workshop.type=='1']

    workshops_final = workshops_type9 + workshops_type8
    if workshops_final and workshops_type7:
        workshop_8 = workshops_final[0]
        point8 = np.array([float(workshop_8.locx), float(workshop_8.locy)])
        points_7 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type7))
        distance = np.sqrt(np.sum((points_7-point8)**2, axis=1))
        workshop_7 = workshops_type7[np.argmin(distance)]
        point7 = np.array([float(workshop_7.locx), float(workshop_7.locy)])
    else:
        workshop_7 = workshops_final[0]
        point7 = np.array([float(workshop_7.locx), float(workshop_7.locy)])
    
    points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
    distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
    workshop_6 = workshops_type6[np.argmin(distance)]
    point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
    
    points_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type5))
    distance = np.sqrt(np.sum((points_5-point7)**2, axis=1))
    workshop_5 = workshops_type5[np.argmin(distance)]
    point5 = np.array([float(workshop_5.locx), float(workshop_5.locy)])
    
    points_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type4))
    distance = np.sqrt(np.sum((points_4-point7)**2, axis=1))
    workshop_4 = workshops_type4[np.argmin(distance)]
    point4 = np.array([float(workshop_4.locx), float(workshop_4.locy)])
    
    points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
    distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
    workshop_3_6 = workshops_type3[np.argmin(distance)]
    
    points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
    distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
    workshop_2_6 = workshops_type2[np.argmin(distance)]
    
    points_3_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
    distance = np.sqrt(np.sum((points_3_5-point5)**2, axis=1))
    workshop_3_5 = workshops_type3[np.argmin(distance)]
    
    points_1_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
    distance = np.sqrt(np.sum((points_1_5-point5)**2, axis=1))
    workshop_1_5 = workshops_type1[np.argmin(distance)]

    points_2_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
    distance = np.sqrt(np.sum((points_2_4-point4)**2, axis=1))
    workshop_2_4 = workshops_type2[np.argmin(distance)]
    
    points_1_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
    distance = np.sqrt(np.sum((points_1_4-point4)**2, axis=1))
    workshop_1_4 = workshops_type1[np.argmin(distance)]
    
    if workshops_final and workshops_type7:
        task = [
            (workshop_1_4.ID, workshop_4.ID),
            (workshop_2_4.ID, workshop_4.ID),
            (workshop_1_5.ID, workshop_5.ID),
            (workshop_3_5.ID, workshop_5.ID),
            (workshop_2_6.ID, workshop_6.ID),
            (workshop_3_6.ID, workshop_6.ID),
            (workshop_4.ID, workshop_7.ID),
            (workshop_5.ID, workshop_7.ID),
            (workshop_6.ID, workshop_7.ID),
            (workshop_7.ID, workshop_8.ID),
        ]
    else:
        task = [
            (workshop_1_4.ID, workshop_4.ID),
            (workshop_2_4.ID, workshop_4.ID),
            (workshop_1_5.ID, workshop_5.ID),
            (workshop_3_5.ID, workshop_5.ID),
            (workshop_2_6.ID, workshop_6.ID),
            (workshop_3_6.ID, workshop_6.ID),
            (workshop_4.ID, workshop_7.ID),
            (workshop_5.ID, workshop_7.ID),
            (workshop_6.ID, workshop_7.ID),
        ]
    return task