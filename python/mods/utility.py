from ctypes import c_float, cdll
import matplotlib.pyplot as plt
from time import perf_counter
class QuickMaths:
    ZoomZoom = False
    @classmethod
    def setZoomZoomState(cls, state : bool):
        cls.ZoomZoom = state
        return state
    @staticmethod
    def speedySqrt(num, speedFactor=0.1):
        """Uses approximation to calculate square root, so the faster the less accurate
        better for problems where precision is not key."""
        if num == 0:
            return 0
        n = num/2
        n2 = n + 1
        while (abs(n - n2) > speedFactor*n):
            xF = num/n
            n2 = n
            n = (n2 + xF) / 2
        return n
def getSpeedData(i, i2, func):
    data = []
    func(0,1)
    for x in range(i):
        data.append([])
        for y in range(i2):
            t = perf_counter()
            func(x, 1)
            deltatime = perf_counter() - t
            data[x].append(deltatime)
    return data

def start():
    l = cdll.LoadLibrary('./mods/speedy.dll').speedy_sqrt
    l.argtypes = [c_float, c_float]
    l.restype = c_float
    mx = (10 ** 4) + 1
    perf1 = getSpeedData(5, mx, l)
    perf2 = getSpeedData(5, mx, QuickMaths.speedySqrt)

    plt.switch_backend('TkAgg')
    fig, axs = plt.subplots(2)
    fig.suptitle('Python vs C compute speed (lower = better)')
    axs[0].title.set_text('C')
    axs[1].title.set_text('Python')
    for i in perf1:
        axs[0].plot(i, marker='.')
        axs[0].legend()
    for j in perf2:
        axs[1].plot(j, marker='.')
        axs[1].legend()
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    plt.show()
    fig.savefig('./Fig.jpg', dpi=fig.dpi, bbox_inches='tight')
