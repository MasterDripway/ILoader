#!py -3.9
import os, platform, psutil
opsys = platform.system()
if opsys == 'Windows':
    import cProfile
class ILoader:
    """Main class"""
    loaded = []
    modules = {}
    if opsys != 'Windows':
        enablestats = False
    else:
        enablestats = True
    @classmethod
    def disablePerformanceStats(cls):
        cls.enablestats = False
    @classmethod
    def getFiles(cls, exclude=[]):
        for r, d, f in os.walk('mods'):
            for fi in f:
                nf = r + '\\' + fi
                if os.path.isfile(nf) and fi not in exclude:
                    cls.loaded.append([r, fi])
        return 
    @classmethod
    def loadFiles(cls, exclude=[]):
        cls.getFiles(exclude)
        if cls.loaded != []:
            for r, m in cls.loaded:
                if m.endswith('.py'):
                    pkg = __import__(r, fromlist=[m])
                    nL = [x[1][:-3] for x in cls.loaded]
                    cls.modules.update({name : module.fromImport({name:classn}) for name, classn in pkg.__dict__.items() if name in nL})
            print(f'{len(cls.modules)} Mods loaded.\nMods loaded:\n{", ".join([str(i) for i in cls.modules])}')
        return
    @classmethod
    def getModules(cls, mod):
        return cls.modules.get(mod, None)
    @classmethod
    def start(cls):
        for modulename, module in cls.modules.items():
            if hasattr(module.properties, 'start'):
                if cls.enablestats: 
                    print(f'Running {modulename} with performance stats on.')
                    p = cProfile.Profile()
                    p.runcall(module.start)
                    print(f'Showing stats for module <{modulename}>')
                    p.print_stats()
                else:    
                    print(f'Running {modulename} without performance analytics.')
                    module.start()
            else:
                print(f'Module {modulename} is set to pkg mode.')
    @classmethod
    def getReourceValues(cls):
        if cls.enablestats:
            rsrcs = {'cpu' : psutil.cpu_percent(), 'mem' : psutil.virtual_memory().percent}
            for i in rsrcs:
                print(i + ': ' + str(rsrcs[i]) + '%')


class module:
    def __init__(self, name, base) -> None:
        self.__name = name
        self.properties = base
        if hasattr(self.properties, 'start'):
            self._isPkg = False
        else:
            self._isPkg = True
    
    @classmethod
    def fromImport(cls, Inherit : dict):
        nm, val = next(iter(Inherit.items()))
        return module(nm, val)
    def start(self):
        if not self._isPkg:
            self.properties.start()



def main():
    ILoader.loadFiles(exclude=["utility.py", "test.py", "shellui.py"])
    ILoader.disablePerformanceStats()
    ILoader.start()
    ILoader.getReourceValues()



if __name__ == '__main__':
    main()    
