class Dispatcher:

    def reg(self,cmd,fn):
        setattr(Dispatcher,cmd,fn)
    def run(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == "quit":
                break
            getattr(self,cmd,self.defaultfn)
    def defaultfn(self):
        print("unknown command")
