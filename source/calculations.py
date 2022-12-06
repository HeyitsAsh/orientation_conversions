import math

def euler_to_quaternion(yaw: float, #yaw in radian
                        pitch: float, #yaw in radian
                        roll: float #yaw in radian
                        ):

    cy = math.cos(pitch/2)
    cp = math.cos(yaw/2)
    cr = math.cos(roll/2)
    sy = math.sin(pitch/2)
    sp = math.sin(yaw/2)
    sr = math.sin(roll/2)

    w = round(cy*cp*cr - sy*sp*sr, 12)
    x = round(sy*sp*cr + cy*cp*sr, 12)
    y = round(sy*cp*cr + cy*sp*sr, 12)
    z = round(cy*sp*cr - sy*cp*sr, 12)

    return w, x, y, z

def quaternion_to_euler(w: float,
                        x: float,
                        y: float,
                        z: float):

    if(abs(round(x*y + z*w, 3)) == 0.5):
        pitch = (2*(x*y + z*w)) * 2 * math.atan2(x, w)
        roll = 0.0
    else:
        pitch = math.atan2(2*y*w - 2*x*z, 1 - 2*y**2 - 2*z**2)
        roll = math.atan2(2*x*w - 2*y*z, 1 - 2*x**2 - 2*z**2)
    
    yaw = math.asin(round(2*x*y + 2*z*w, 3))
    
    return yaw, pitch, roll


def quaternion_to_rotmat(w: float,
                         x: float,
                         y: float,
                         z: float):
    #quaternion Q = w + xi + yj + zk

    # 1 - 2*qy2 - 2*qz2	    2*qx*qy - 2*qz*qw	2*qx*qz + 2*qy*qw
    # 2*qx*qy + 2*qz*qw	    1 - 2*qx2 - 2*qz2	2*qy*qz - 2*qx*qw
    # 2*qx*qz - 2*qy*qw	    2*qy*qz + 2*qx*qw	1 - 2*qx2 - 2*qy2
    r1 = [round(1 - 2*y**2 - 2*z**2, 12), round(2*x*y - 2*z*w, 12), round(2*x*z + 2*y*w, 12)]
    r2 = [round(2*x*y + 2*z*w, 12), round(1 - 2*x**2 - 2*z**2, 12), round(2*y*z - 2*x*w, 12)]
    r3 = [round(2*x*z - 2*y*w, 12), round(2*y*z + 2*x*w, 12), round(1 - 2*x**2 - 2*y**2, 12)]

    return [r1,r2,r3]

def euler_to_rotmat(yaw: float, #yaw in radian
                    pitch: float, #yaw in radian
                    roll: float #yaw in radian
                    ):
    sa = math.sin(yaw)
    ca = math.cos(yaw)
    sb = math.sin(roll)
    cb = math.cos(roll)
    sh = math.sin(pitch)
    ch = math.cos(pitch)

    #   ch*ca	                -ch*sa*cb + sh*sb	            ch*sa*sb + sh*cb
    #   sa	                    ca*cb	                        -ca*sb
    #   -sh*ca	                sh*sa*cb + ch*sb	            -sh*sa*sb + ch*cb
    r1 = [round(ch*ca, 12),     round(-ch*sa*cb + sh*sb, 12),   round(ch*sa*sb + sh*cb, 12)]
    r2 = [round(sa, 12),        round(ca*cb, 12),               round(-ca*sb, 12)]
    r3 = [round(-sh*ca, 12),    round(sh*sa*cb + ch*sb, 12),    round(-sh*sa*sb + ch*cb, 12)]

    return [r1,r2,r3]


def main(): # Test function

    inp = 90 * math.pi / 180
    w,x,y,z = euler_to_quaternion(inp, 0, 0)
    print(w,x,y,z)
    
    yaw, p, r = quaternion_to_euler(w,x,y,z)
    print(yaw*180/math.pi, p*180/math.pi, r*180/math.pi)

    rot_mat_q = quaternion_to_rotmat(w,x,y,z)
    print("Quat to rotation")
    for x in rot_mat_q:
        print(x, end = '\n')

    rot_mat_e = euler_to_rotmat(yaw, p, r)
    print("Euler to rotation")
    for x in rot_mat_e:
        print(x, end = '\n')

if __name__ == '__main__':
    main()



#https://www.euclideanspace.com/maths/standards/index.htm