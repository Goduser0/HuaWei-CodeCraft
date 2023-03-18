import sys
import numpy as np

# v4***********************************************************************************************************
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

# v1************************************************************************************************************
def cal_distance(loc0x, loc0y, loc1x, loc1y):
    return float(np.sqrt((float(loc0x)-float(loc1x))**2 + (float(loc0y)-float(loc1y))**2))

def tasks_sort(*workshops):
    workshops_type1, workshops_type2, workshops_type3, workshops_type4, workshops_type5, workshops_type6, workshops_type7, workshops_type8, workshops_type9 = [], [], [], [], [], [], [], [], []

    for workshop in workshops:
        if str(workshop.type)=='9': 
            workshops_type9.append(workshop)
        elif str(workshop.type)=='8': 
            workshops_type8.append(workshop)
        elif str(workshop.type)=='7': 
            workshops_type7.append(workshop)
        elif str(workshop.type)=='6': 
            workshops_type6.append(workshop)
        elif str(workshop.type)=='5': 
            workshops_type5.append(workshop)
        elif str(workshop.type)=='4': 
            workshops_type4.append(workshop)
        elif str(workshop.type)=='3': 
            workshops_type3.append(workshop)
        elif str(workshop.type)=='2': 
            workshops_type2.append(workshop)
        elif str(workshop.type)=='1': 
            workshops_type1.append(workshop)
            
    tasks = []
    for workshop_type7 in workshops_type7:
        if str(workshop_type7.out_status) == '1':         
            distance_7_8 = []
            for workshop_type8 in workshops_type8:
                num_bin = bin(int(str(workshop_type8.in_status), 10))
                if len(num_bin)<10 or num_bin[-8] == '0':
                    distance_7_8.append((workshop_type8.ID, cal_distance(workshop_type7.locx, workshop_type7.locy, workshop_type8.locx, workshop_type8.locy)))
            distance_7_8 = np.sort(np.array(distance_7_8, dtype=np.dtype([("id", int), ("distance", float)])), order="distance")
            if distance_7_8.size > 0:
                tasks.append((workshop_type7.ID, distance_7_8[0][0]))
    
    for workshop_type6 in workshops_type6:
        if str(workshop_type6.out_status) == '1':         
            distance_6_7 = []
            for workshop_type7 in workshops_type7:
                num_bin = bin(int(str(workshop_type7.in_status), 10))
                if len(num_bin)<9 or num_bin[-7] == '0':
                    distance_6_7.append((workshop_type7.ID, cal_distance(workshop_type6.locx, workshop_type6.locy, workshop_type7.locx, workshop_type7.locy)))
            distance_6_7 = np.sort(np.array(distance_6_7, dtype=np.dtype([("id", int), ("distance", float)])), order="distance")
            if distance_6_7.size > 0:
                tasks.append((workshop_type6.ID, distance_6_7[0][0]))
    
    for workshop_type5 in workshops_type5:
        if str(workshop_type5.out_status) == '1':         
            distance_5_7 = []
            for workshop_type7 in workshops_type7:
                num_bin = bin(int(str(workshop_type7.in_status), 10))
                if len(num_bin)<8 or num_bin[-6] == '0':
                    distance_5_7.append((workshop_type7.ID, cal_distance(workshop_type5.locx, workshop_type5.locy, workshop_type7.locx, workshop_type7.locy)))
            distance_5_7 = np.sort(np.array(distance_5_7, dtype=np.dtype([("id", int), ("distance", float)])), order="distance")
            if distance_5_7.size > 0:    
                tasks.append((workshop_type5.ID, distance_5_7[0][0]))            
    
    for workshop_type4 in workshops_type4:
        if str(workshop_type4.out_status) == '1':         
            distance_4_7 = []
            for workshop_type7 in workshops_type7:
                num_bin = bin(int(str(workshop_type8.in_status), 10))
                if len(num_bin)<7 or num_bin[-5] == '0':
                    distance_4_7.append((workshop_type7.ID, cal_distance(workshop_type4.locx, workshop_type4.locy, workshop_type7.locx, workshop_type7.locy)))
            distance_4_7 = np.sort(np.array(distance_4_7, dtype=np.dtype([("id", int), ("distance", float)])), order="distance")
            if distance_4_7.size > 0:
                tasks.append((workshop_type4.ID, distance_4_7[0][0]))  
    
    for workshop_type3 in workshops_type3:
        if str(workshop_type3.out_status) == '1':
            distance_3_56 = []
            for workshop_type5 in workshops_type5:
                num_bin = bin(int(str(workshop_type5.in_status), 10))
                if len(num_bin)<6 or num_bin[-4] == '0':
                    distance_3_56.append((workshop_type5.ID, cal_distance(workshop_type3.locx, workshop_type3.locy, workshop_type5.locx, workshop_type5.locy)))
            for workshop_type6 in workshops_type6:
                num_bin = bin(int(str(workshop_type6.in_status), 10))
                if len(num_bin)<6 or num_bin[-4] == '0':
                    distance_3_56.append((workshop_type6.ID, cal_distance(workshop_type3.locx, workshop_type3.locy, workshop_type6.locx, workshop_type6.locy)))
            distance_3_56 = np.sort(np.array(distance_3_56, dtype=np.dtype([("id", int), ("distance", float)])), order="distance")
            if distance_3_56.size >  0:   
                tasks.append((workshop_type3.ID, distance_3_56[0][0]))
            
    for workshop_type2 in workshops_type2:
        if str(workshop_type2.out_status) == '1':
            distance_2_46 = []
            for workshop_type4 in workshops_type4:
                num_bin = bin(int(str(workshop_type4.in_status), 10))
                if len(num_bin)<5 or num_bin[-3] == '0':
                    distance_2_46.append((workshop_type4.ID, cal_distance(workshop_type2.locx, workshop_type2.locy, workshop_type4.locx, workshop_type4.locy)))
            for workshop_type6 in workshops_type6:
                num_bin = bin(int(str(workshop_type6.in_status), 10))
                if len(num_bin)<5 or num_bin[-3] == '0':
                    distance_2_46.append((workshop_type6.ID, cal_distance(workshop_type2.locx, workshop_type2.locy, workshop_type6.locx, workshop_type6.locy)))
            distance_2_46 = np.sort(np.array(distance_2_46, dtype=np.dtype([("id", int), ("distance", float)])), order="distance")
            if distance_2_46.size > 0:
                tasks.append((workshop_type2.ID, distance_2_46[0][0]))
            
    for workshop_type1 in workshops_type1:
        if str(workshop_type1.out_status) == '1':
            distance_1_45 = []
            for workshop_type4 in workshops_type4:
                num_bin = bin(int(str(workshop_type4.in_status), 10))
                if len(num_bin)<4 or num_bin[-2] == '0':
                    distance_1_45.append((workshop_type4.ID, cal_distance(workshop_type1.locx, workshop_type1.locy, workshop_type4.locx, workshop_type4.locy)))
            for workshop_type5 in workshops_type5:
                num_bin = bin(int(str(workshop_type5.in_status), 10))
                if len(num_bin)<4 or num_bin[-2] == '0':
                    distance_1_45.append((workshop_type5.ID, cal_distance(workshop_type1.locx, workshop_type1.locy, workshop_type5.locx, workshop_type5.locy)))
            distance_1_45 = np.sort(np.array(distance_1_45, dtype=np.dtype([("id", int), ("distance", float)])), order="distance")
            if distance_1_45.size > 0: 
                tasks.append((workshop_type1.ID, distance_1_45[0][0]))      
    
    return tasks


# v2***********************************************************************************************************
def tasks_sort(*workshops):
    task = []
    workshops_out = [workshop for workshop in workshops if workshop.out_status=='1']
    workshops_type8 = [workshop for workshop in workshops if workshop.type=='8']
    workshops_type7 = [workshop for workshop in workshops if workshop.type=='7']
    workshops_type6 = [workshop for workshop in workshops if workshop.type=='6']
    workshops_type5 = [workshop for workshop in workshops if workshop.type=='5']
    workshops_type4 = [workshop for workshop in workshops if workshop.type=='4']

    if workshops_out:
        workshops_out.sort(key = lambda x: x.type, reverse=True)
        workshops_out_task = workshops_out[:4]
        sys.stderr.write(workshops_out_task[0].ID)
        for workshop_out_task in workshops_out_task:
            query_point = np.array([float(workshop_out_task.locx), float(workshop_out_task.locy)])
            if workshop_out_task.type == '7':
                num = 0b10000000
                workshops_7_8 = [workshop for workshop in workshops_type8 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_7_8))
                distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                workshop_in_task = workshops_7_8[np.argmin(distance)]
                
            elif workshop_out_task.type == '6':
                num = 0b01000000
                workshops_6_7 = [workshop for workshop in workshops_type7 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                if workshops_6_7: 
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_6_7))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_6_7[np.argmin(distance)]
                else:
                    continue
                
            elif workshop_out_task.type == '5':
                num = 0b00100000
                workshops_5_7 = [workshop for workshop in workshops_type7 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                if workshops_5_7:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_5_7))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_5_7[np.argmin(distance)]
                else:
                    continue
                
            elif workshop_out_task.type == '4':
                num = 0b00010000
                workshops_4_7 = [workshop for workshop in workshops_type7 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                if workshops_4_7:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_4_7))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_4_7[np.argmin(distance)]
                else:
                    continue
                
            elif workshop_out_task.type == '3':
                num = 0b00001000
                workshops_3_5 = [workshop for workshop in workshops_type5 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                workshops_3_6 = [workshop for workshop in workshops_type6 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                workshops_3_56 = workshops_3_5 + workshops_3_6
                if workshops_3_56:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_3_56))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_3_56[np.argmin(distance)]
                else:
                    continue
                
            elif workshop_out_task.type == '2':
                num = 0b00000100
                workshops_2_4 = [workshop for workshop in workshops_type4 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                workshops_2_6 = [workshop for workshop in workshops_type6 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                workshops_2_46 = workshops_2_4 + workshops_2_6
                if workshops_2_46:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_2_46))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_2_46[np.argmin(distance)]
                else:
                    continue
                    
            elif workshop_out_task.type == '1':
                num = 0b00000010
                workshops_1_4 = [workshop for workshop in workshops_type4 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                workshops_1_5 = [workshop for workshop in workshops_type5 if int(bin(int(workshop.in_status, 10)), 2)&num == 0]
                workshops_1_45 = workshops_1_4 + workshops_1_5
                if workshops_1_45:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_1_45))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_1_45[np.argmin(distance)]
                else:
                    continue
                
            task.append((workshop_out_task.ID, workshop_in_task.ID))
            
    return task

# v3 **************************************************************************************************************
def tasks_sort(*workshops):
    task = []
    workshops = list(workshops)
    workshops_sort_by_in = workshops.sort(key = lambda x:int(x.in_status), reverse=True)
    
    workshops_sort_by_out = [workshop for workshop in workshops if workshop.out_status=='1']
    
    if workshops_sort_by_out:
        workshops_sort_by_out.sort(key = lambda x: int(x.type), reverse=True)
    
    
    workshops_type8 = [workshop for workshop in workshops if workshop.type=='8']
    workshops_type7 = [workshop for workshop in workshops if workshop.type=='7']
    workshops_type6 = [workshop for workshop in workshops if workshop.type=='6']
    workshops_type5 = [workshop for workshop in workshops if workshop.type=='5']
    workshops_type4 = [workshop for workshop in workshops if workshop.type=='4']

    if workshops_sort_by_out:
        workshops_out_task = workshops_sort_by_out[:] 
        for workshop_out_task in workshops_out_task:
            query_point = np.array([float(workshop_out_task.locx), float(workshop_out_task.locy)])
            if workshop_out_task.type == '7':
                num = 0b10000000
                workshops_7_8 = [workshop for workshop in workshops_type8 if (workshop.in_status & num) == 0]
                points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_7_8))
                distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                workshop_in_task = workshops_7_8[np.argmin(distance)]
                
            elif workshop_out_task.type == '6':
                num = 0b01000000
                workshops_6_7 = [workshop for workshop in workshops_type7 if (workshop.in_status & num) == 0]
                if workshops_6_7: 
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_6_7))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_6_7[np.argmin(distance)]
                else:
                    continue
                
            elif workshop_out_task.type == '5':
                num = 0b00100000
                workshops_5_7 = [workshop for workshop in workshops_type7 if (workshop.in_status & num) == 0]
                if workshops_5_7:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_5_7))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_5_7[np.argmin(distance)]
                else:
                    continue
                
            elif workshop_out_task.type == '4':
                num = 0b00010000
                workshops_4_7 = [workshop for workshop in workshops_type7 if (workshop.in_status & num) == 0]
                if workshops_4_7:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_4_7))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_4_7[np.argmin(distance)]
                else:
                    continue
                
            elif workshop_out_task.type == '3':
                num = 0b00001000
                workshops_3_5 = [workshop for workshop in workshops_type5 if (workshop.in_status & num) == 0]
                workshops_3_6 = [workshop for workshop in workshops_type6 if (workshop.in_status & num) == 0]
                workshops_3_56 = workshops_3_5 + workshops_3_6
                if workshops_3_56:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_3_56))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_3_56[np.argmin(distance)]
                else:
                    continue
                
            elif workshop_out_task.type == '2':
                num = 0b00000100
                workshops_2_4 = [workshop for workshop in workshops_type4 if (workshop.in_status & num) == 0]
                workshops_2_6 = [workshop for workshop in workshops_type6 if (workshop.in_status & num) == 0]
                workshops_2_46 = workshops_2_4 + workshops_2_6
                if workshops_2_46:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_2_46))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_2_46[np.argmin(distance)]
                else:
                    continue
                    
            elif workshop_out_task.type == '1':
                num = 0b00000010
                workshops_1_4 = [workshop for workshop in workshops_type4 if (workshop.in_status & num) == 0]
                workshops_1_5 = [workshop for workshop in workshops_type5 if (workshop.in_status & num) == 0]
                workshops_1_45 = workshops_1_4 + workshops_1_5
                if workshops_1_45:
                    points = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_1_45))
                    distance = np.sqrt(np.sum((points-query_point)**2, axis=1))
                    workshop_in_task = workshops_1_45[np.argmin(distance)]
                else:
                    continue
                
            task.append((workshop_out_task.ID, workshop_in_task.ID))
            
    return task
