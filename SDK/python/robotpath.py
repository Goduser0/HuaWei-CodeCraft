import sys
import numpy as np
import math


max_linear_velocity = 6
max_angular_velocity = math.pi

def pid_control(error, integral_error, pre_error, type, carry):
    if carry:
        if type == 'v':
            k_p = 9.0
            k_i = 0.0
            k_d = 0.0
        if type == 'w':
            k_p = 10.0
            k_i = 0.0
            k_d = 5.0
    else:
        if type == 'v':
            k_p = 9.0
            k_i = 0.0
            k_d = 0.0
        if type == 'w':
            k_p = 10.0
            k_i = 0.0
            k_d = 5.0
    integral_error += error
    integral_error = min(integral_error, 10.0)
    derivative_error = error - pre_error
    control = k_p * error + k_i * integral_error + k_d * derivative_error
    pre_error = error
    return control, integral_error, pre_error

def error_check(error):
    if error > math.pi:
        error -= 2*math.pi
    elif error < -math.pi:
        error += 2*math.pi
    
    return error 

def robot_control(robot, *frame_workshop_status):
    if robot.target_ID:
        target_x = float(frame_workshop_status[int(robot.target_ID)].locx)
        target_y = float(frame_workshop_status[int(robot.target_ID)].locy)
        current_x = float(robot.locx)
        current_y = float(robot.locy)
        current_toward = float(robot.toward)
        
        current_vx = float(robot.line_speed_x)
        current_vy = float(robot.line_speed_y)
        current_w = float(robot.angle_speed)

        dx = target_x - current_x
        dy = target_y - current_y
        angle_target = math.atan2(dy, dx)
        angle_v = math.atan2(current_vy, current_vx)
        angle_toward = current_toward
        
        error_distance = math.sqrt(dx**2 + dy**2)
        error_target2toward = error_check(angle_target - angle_toward)
        
        if robot.carry != '0':
            current_v, robot.v_integral_error, robot.v_prev_error = pid_control(error_distance, robot.v_integral_error, robot.v_prev_error, 'v', True)
            current_w, robot.w_integral_error, robot.w_prev_error = pid_control(error_target2toward, robot.w_integral_error, robot.w_prev_error, 'w', True)
        else:
            current_v, robot.v_integral_error, robot.v_prev_error = pid_control(error_distance, robot.v_integral_error, robot.v_prev_error, 'v', False)
            current_w, robot.w_integral_error, robot.w_prev_error = pid_control(error_target2toward, robot.w_integral_error, robot.w_prev_error, 'w', False)
        
        workshops_type7 = [workshop_i for workshop_i in frame_workshop_status if workshop_i.type == '7']
        
        # map1
        if len(workshops_type7) == 8:
            if abs(robot.w_prev_error) < math.pi*0.8:
                linear_velocity = str(current_v)
            else:
                linear_velocity = str(min(current_v, 1.0))
            angular_velocity = str(current_w)
        # map3
        elif len(workshops_type7) == 0:
            if abs(error_distance) <= 1.5:
                linear_velocity = str(min(current_v, 2.0))
            else:
                linear_velocity = str(min(current_v, max_linear_velocity))
            angular_velocity = str(min(current_w, max_angular_velocity))
        # map4
        elif len(workshops_type7) == 1:
            # if abs(error_distance) <= 2.0:
            #     linear_velocity = str(min(current_v, 5.5))
            # else:
            #     linear_velocity = str(min(current_v, max_linear_velocity))
            linear_velocity = str(min(current_v, max_linear_velocity))
            angular_velocity = str(min(current_w, max_angular_velocity))
        # map2    
        else:
            if abs(error_distance) <= 2.0:
                linear_velocity = str(min(current_v, 5.5))
            else:
                linear_velocity = str(min(current_v, max_linear_velocity))
            # linear_velocity = str(min(current_v, max_linear_velocity))
            angular_velocity = str(min(current_w, max_angular_velocity))
    else:
        linear_velocity = '0'
        angular_velocity = '0'
    return [linear_velocity, angular_velocity]