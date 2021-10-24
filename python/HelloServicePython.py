from com.v2.migration.services import HelloService

class HelloServicePython(HelloService):
    def __init__(self):
        self.value="Hello from python"

    def getHello(self):
        return self.value