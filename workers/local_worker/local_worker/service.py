from nameko.rpc import rpc, RpcProxy
from nameko.events import EventDispatcher
from time import time
import datetime


class Time(object):
    name = "local_time_service"
    # say = RpcProxy('say')

    @rpc
    def local(self):
        print("CZAS", datetime.datetime.fromtimestamp(time()).isoformat())
        mytime = datetime.datetime.fromtimestamp(time()).isoformat()
        
        return mytime

class Say(object):
    name = "say_wow_service"

    @rpc
    def say(self, text1):    
        response = "WOW, Say {}".format(text1)
        return response