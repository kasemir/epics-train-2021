from pcaspy import SimpleServer, Driver
import demo

pvdb = {
    'random' : {
        # 'desc': 'return value between 0 and hilim'
        'type'  : 'float',
        'hilim' : 10,
    },
}

class DemoDriver(Driver):
    def __init__(self):
        super(DemoDriver, self).__init__()

    def read(self, reason):
        if reason == 'random':
            limit = self.getParamInfo(reason)['hilim']
            value = demo.getRandom(limit)
        else:
            value = self.getParam(reason)
        return value

if __name__ == '__main__':
    server = SimpleServer()
    server.createPV('training:pcaspy:', pvdb)
    driver = DemoDriver()
    while True:
        # process CA transactions
        server.process(0.1)
