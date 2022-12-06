import math
import decimal
from decimal import Decimal

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

    w = Decimal(str(cy*cp*cr - sy*sp*sr)).__float__()
    x = Decimal(str(sy*sp*cr + cy*cp*sr)).__float__()
    y = Decimal(str(sy*cp*cr + cy*sp*sr)).__float__()
    z = Decimal(str(cy*sp*cr - sy*cp*sr)).__float__()

    return w, x, y, z

def quaternion_to_euler(w: float,
                        x: float,
                        y: float,
                        z: float):

    if(abs(Decimal(str(x*y + z*w)).__float__()) == 0.5):
        pitch = (2*(x*y + z*w)) * 2 * math.atan2(x, w)
        roll = 0.0
    else:
        pitch = math.atan2(2*y*w - 2*x*z, 1 - 2*y**2 - 2*z**2)
        roll = math.atan2(2*x*w - 2*y*z, 1 - 2*x**2 - 2*z**2)
    
    if(Decimal(str(2*x*y + 2*z*w)).__float__() <= Decimal('1.0')):
        yaw = math.asin(Decimal(str(2*x*y + 2*z*w)).__float__())
    else:
        if(Decimal(str(2*x*y + 2*z*w)).__float__() < Decimal('1.0005')):
            yaw = math.asin(1.0)
        else:
            raise ValueError("math domain error - not in [-1,1]")
    
    return yaw, pitch, roll


def quaternion_to_rotmat(w: float,
                         x: float,
                         y: float,
                         z: float):
    #quaternion Q = w + xi + yj + zk

    # 1 - 2*qy2 - 2*qz2	    2*qx*qy - 2*qz*qw	2*qx*qz + 2*qy*qw
    # 2*qx*qy + 2*qz*qw	    1 - 2*qx2 - 2*qz2	2*qy*qz - 2*qx*qw
    # 2*qx*qz - 2*qy*qw	    2*qy*qz + 2*qx*qw	1 - 2*qx2 - 2*qy2
    r1 = [Decimal(str(1 - 2*y**2 - 2*z**2)).__float__(), Decimal(str(2*x*y - 2*z*w)).__float__(), Decimal(str(2*x*z + 2*y*w)).__float__()]
    r2 = [Decimal(str(2*x*y + 2*z*w)).__float__(), Decimal(str(1 - 2*x**2 - 2*z**2)).__float__(), Decimal(str(2*y*z - 2*x*w)).__float__()]
    r3 = [Decimal(str(2*x*z - 2*y*w)).__float__(), Decimal(str(2*y*z + 2*x*w)).__float__(), Decimal(str(1 - 2*x**2 - 2*y**2)).__float__()]

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
    r1 = [Decimal(str(ch*ca)).__float__(),     Decimal(str(-ch*sa*cb + sh*sb)).__float__(),   Decimal(str(ch*sa*sb + sh*cb)).__float__()]
    r2 = [Decimal(str(sa)).__float__(),        Decimal(str(ca*cb)).__float__(),               Decimal(str(-ca*sb)).__float__()]
    r3 = [Decimal(str(-sh*ca)).__float__(),    Decimal(str(sh*sa*cb + ch*sb)).__float__(),    Decimal(str(-sh*sa*sb + ch*cb)).__float__()]

    return [r1,r2,r3]


def main(): # Test function
    decimal.ROUND_05UP

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