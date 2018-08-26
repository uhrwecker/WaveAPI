import numpy as np

'''
(1)
dh/dt = - dvx/dx * h - dh/dx * vx - dvy/dy h - dh/dy vy
(2)
'''

def d_dx(vector, dx=1):
    return np.gradient(vector, axis=0)

def d_dy(vector, dy=1):
    return np.gradient(vector, axis=1)
    

def dh_dt(h, vx, vy, h_lvl=0.9):
    return - h_lvl * (d_dx(vx) + d_dy(vy))

#def dvy_dt(h, vx, vy, b):
#    sum1 = - dh_dt(h, vx, vy) * vx
#    sum2 = - d_dx(h) * d_dx(d_dx(vx))
#    sum3 = - h * (d_dy(vy) * vx + d_dy(vx) * vy)
#    sum4 = - 0.5 * 0.9 * d_dx(h*h)
#    sum5 = - 0.9 * h * d_dx(b)
#    return 1/h * (sum1 + sum2 + sum3 + sum4 + sum5)

#def dvx_dt(h, vx, vy, b):
#    sum1 = - dh_dt(h, vx, vy) * vy
#    sum2 = - d_dy(h) * d_dy(d_dy(vy))
#    sum3 = - h * (d_dx(vy) * vx + d_dx(vx) * vy)
#    sum4 = - 0.5 * 0.9 * d_dy(h*h)
#    sum5 = - 0.9 * h * d_dy(b)
#    return 1/h * (sum1 + sum2 + sum3 + sum4 + sum5)

def dvx_dt(h, vx, vy, b):
    return - 10 * d_dx(h) - 0.01 * vx

def dvy_dt(h, vx, vy, b):
    return - 10 * d_dy(h) - 0.01 * vy

def get_next_vx(h, vx, vy, b, dt=1):
    return dvx_dt(h, vx, vy, b) * dt + vx

def get_next_vy(h, vx, vy, b, dt=1):
    return dvy_dt(h, vx, vy, b) * dt + vy

def get_next_h(h, vx, vy, dt=1):
    return dh_dt(h, vx, vy) * dt + h

def main():
    from matplotlib import pyplot, cm
    from mpl_toolkits.mplot3d import Axes3D

    nx = 16
    ny = 16

    b = np.zeros(shape=(nx, ny))
    b[:,:] = 0.1
    vx = np.zeros(shape=(nx, ny))
    vx[:,0] = 0.1
    vy = np.zeros(shape=(nx, ny))
    #vy[:,:] = 0.1
    h = np.zeros(shape=(nx, ny))
    h[:, 0] = 0.1

    vx = get_next_vx(h, vx, vy, b)
    print(vx)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)
    
    print(vx)
    vx = get_next_vx(h, vx, vy, b)
    print(vx)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    vx = get_next_vx(h, vx, vy, b)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    vx = get_next_vx(h, vx, vy, b)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    vx = get_next_vx(h, vx, vy, b)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    vx = get_next_vx(h, vx, vy, b)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    vx = get_next_vx(h, vx, vy, b)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    print(vx)

    vx = get_next_vx(h, vx, vy, b)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    vx = get_next_vx(h, vx, vy, b)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    vx = get_next_vx(h, vx, vy, b)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    vx = get_next_vx(h, vx, vy, b)
    vy = get_next_vy(h, vx, vy, b)
    h = get_next_h(h, vx, vy)

    

    fig = pyplot.figure()
    ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(np.linspace(0, nx, nx), np.linspace(0, ny, ny))
    surf = ax.plot_surface(X, Y, h[:], rstride=1, cstride=1, antialiased=True)
    #ax.set_zlim(1, 2.5)
    pyplot.show()

if __name__ == '__main__':
    main()

