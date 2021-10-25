from com.v2.migration.services import HelloService
# from com.
# import io
# import com
# import requests
# import json
# import os
# import asyncio
# import time

class HelloServicePython(HelloService):
    def __init__(self):
        self.value="Hello from python"

    def getHello(self):
        return self.value