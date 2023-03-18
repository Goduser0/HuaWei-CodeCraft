import sys
import numpy as np

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
                workshops_7_8 = workshops_type8
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