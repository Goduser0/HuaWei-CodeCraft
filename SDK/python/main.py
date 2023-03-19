#!/bin/bash
import sys
import numpy as np
# Delete before using
import time
# import threading
from tasks import framework_search
from cmd import read_util_ok, finish
from robotpath import robot_control

class workshop(object):
    def __init__(self, ID, type, locx, locy, res_time, in_status, out_status):
        self.ID = ID
        self.type = type
        self.locx = locx
        self.locy = locy
        self.res_time = res_time
        self.in_status = in_status
        self.out_status = out_status

class robot(object):
    def __init__(self, ID, task=None, target_ID=None, v_integral_error=0.0, v_prev_error=0.0, w_integral_error=0.0, w_prev_error=0.0):
        self.ID = ID
        self.task = task
        self.target_ID = target_ID
        self.v_integral_error = v_integral_error
        self.v_prev_error = v_prev_error
        self.w_integral_error = v_integral_error
        self.w_prev_error =v_prev_error
        
    def add(self, in_workshop_id, carry, alpha, beta, angle_speed, line_speed_x, line_speed_y, toward, locx, locy):
        self.in_work_shop_id = in_workshop_id
        self.carry = carry
        self.alpha = alpha
        self.beta = beta
        self.angle_speed = angle_speed
        self.line_speed_x = line_speed_x
        self.line_speed_y = line_speed_y
        self.toward = toward
        self.locx = locx
        self.locy = locy

if __name__ == '__main__':
    test = False
    frame_robot_status = [robot('0'), robot('1'), robot('2'), robot('3')]
    read_util_ok()  # 初始化时读入地图数据，直到OK结束
    finish()        # 初始化完成
    tasks = []
    task_tree = []
    v_integral_error = 0.0
    v_prev_error = 0.0
    w_integral_error = 0.0
    w_prev_error = 0.0
    
    while True:
        # 获取帧序号和当前金钱数
        line1 = sys.stdin.readline().strip().split(' ')
        if len(line1) >=2:
            frame_id = line1[0]
            frame_coins = int(line1[1])
        if test:
            sys.stderr.write(frame_id+' '+str(frame_coins)+'\n')
        
        # 获取场上workshop数量
        line2 = sys.stdin.readline().strip()
        if line2:
            K = line2
        if test:
            sys.stderr.write(str(line2)+'\n')
        
        # 获取场上workshop状态
        frame_workshop_status = []
        for k in range(int(K)):
            frame_workshop_status.append(sys.stdin.readline().strip())
            if test:
                sys.stderr.write(str(frame_workshop_status[k])+'\n')
            parts = frame_workshop_status[k].split(' ')
            frame_workshop_status[k] = workshop(
                str(k),
                parts[0],
                parts[1],
                parts[2],
                parts[3], 
                int(bin(int(parts[4], 10)), 2), 
                parts[5],
                )
        
        # 获取场上robot状态
        for i in range(4):
            line = sys.stdin.readline().strip()
            if test:
                sys.stderr.write(str(line)+'\n')
            parts = line.split(' ')
            frame_robot_status[i].add(
                parts[0],
                parts[1],
                parts[2],
                parts[3],
                parts[4],
                parts[5],
                parts[6],
                parts[7],
                parts[8],
                parts[9],
            )         
        if test:
            sys.stderr.write('--------------------------------------------'+'\n') 
            
        # frame_robot_status                                                                                                                                     
        
        # 忽略其他输入数据，读到OK为止
        read_util_ok()
    
        # 指令下发
        task_tree = framework_search(*frame_workshop_status)
        
           
        if len(tasks) <= 4:
            for i in task_tree[:6]:
                tasks.append((i[0].ID, i[1].ID))
        else:
            pass
        
        task_level2 = task_tree[6:9]
        for part in task_level2:
            if part[0].out_status == '1' and ((part[0].ID, part[1].ID) not in tasks):
                signal = True
                for r in frame_robot_status:
                    if r.task == (part[0].ID, part[1].ID):
                        signal = False
                if signal:
                    tasks.insert(0, (part[0].ID, part[1].ID))
                    
        task_level3 = task_tree[9]
        if task_level3[0].out_status == '1' and ((task_level3[0].ID, task_level3[1].ID) not in tasks):
            signal = True
            for r in frame_robot_status:
                if r.task == (task_level3[0].ID, task_level3[1].ID):
                    signal = False
            if signal:
                tasks.insert(0, (task_level3[0].ID, task_level3[1].ID))
            
        
        # 显示任务分配策略
        # sys.stderr.write('task:' + str(frame_id) + '\n')
        # for task in tasks:
        #     sys.stderr.write(str(task[0]) + '->' + str(task[1]) + '\n')
        
        # 显示robot的任务
        sys.stderr.write('task:' + str(frame_id) + '\n')
        for robot in frame_robot_status:
            if robot.task:
                sys.stderr.write(robot.ID + ':' + robot.task[0] + '->' + robot.task[1] + '\n')
            else:
                sys.stderr.write(robot.ID + ': None' + '\n')
        
        # 指令输出
        sys.stdout.write(frame_id + '\n')
          
        i = 0
        for robot_i in frame_robot_status: 
            if robot_i.task:
                if robot_i.carry != '0':
                    if robot_i.in_work_shop_id == robot_i.task[1]:
                        sys.stdout.write('sell ' + str(i) + '\n')
                        sys.stdout.write('forward ' + str(i) + ' 0'+'\n')
                        sys.stdout.write('rotate '+ str(i) + ' 0'+'\n')
                        robot_i.task = None
                        robot_i.target_ID = None  
                    else:    
                        robot_i.target_ID = robot_i.task[1]
                        args = robot_control(robot_i, *frame_workshop_status)
                        sys.stdout.write('forward '+ str(i) + ' ' + args[0] +'\n')
                        sys.stdout.write('rotate ' + str(i) + ' ' + args[1] +'\n')
                else:
                    if robot_i.in_work_shop_id == robot_i.task[0]:
                        sys.stdout.write('buy '+ str(i) + '\n')
                        sys.stdout.write('forward ' + str(i) + ' 0' + '\n')
                        sys.stdout.write('rotate ' + str(i) + ' 0' + '\n')
                        robot_i.target_ID = robot_i.task[1]

                    else:
                        robot_i.target_ID = robot_i.task[0]
                        args = robot_control(robot_i, *frame_workshop_status)
                        sys.stdout.write('forward '+ str(i) + ' ' + args[0] +'\n')
                        sys.stdout.write('rotate ' + str(i) + ' ' + args[1] +'\n')
            else:
                if len(tasks) != 0:
                    robot_i.task = tasks[0]
                    tasks = tasks[1:]
                    
                    robot_i.target_ID = robot_i.task[0]
                    args = robot_control(robot_i, *frame_workshop_status)
                    sys.stdout.write('forward '+ str(i) + ' ' + args[0]+'\n')
                    sys.stdout.write('rotate ' + str(i) + ' ' + args[1] +'\n')
            i+=1

        finish()
        