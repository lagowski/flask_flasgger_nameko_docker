from nameko.rpc import rpc, RpcProxy
from time import time
import datetime


class Time(object):
    name = "local_time_service"

    @rpc
    def local(self):
        mytime = datetime.datetime.fromtimestamp(time()).isoformat()
        return mytime

class Say(object):
    name = "say_wow_service"

    @rpc
    def say(self, text1):    
        response = "WOW, Say {}".format(text1)
        return response