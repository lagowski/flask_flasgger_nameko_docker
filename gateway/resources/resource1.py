from flask_restful import Resource, fields, marshal_with, reqparse
from nameko.standalone.rpc import ServiceRpcProxy, ClusterRpcProxy
from dotenv import load_dotenv
from nameko.rpc import RpcProxy
from flasgger import swag_from
import os

text2say_fields = {
    "text2say": fields.String,
}

time_fields = {
    "time": fields.String,
}

# First Option if using ClusterProxy
CONFIG={'AMQP_URI': "pyamqp://user:pass@rabbit"}

# Second Option if using ServiceRpcProxy (with context)
def rpc_proxy(service):
    print("Service:", service)
    config = {'AMQP_URI': os.getenv('AMQP_URI')}
    return ServiceRpcProxy(service, config)

# load .env vars
current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path="{}/.env_service2".format(current_dir))

class Say(Resource):

    # @swag_from('./resource1.yml')
    @marshal_with(text2say_fields)
    def get(self, text2say="No text"):
        '''
        Get a Example saying sended text
          ---
          tags:
            - say
          produces:
            - application/json
            - application/xml
          parameters:
            - in: path
              name: text2say
              description: Text to return
              type: string
              required: false
          responses:
            200:
              description: OK
              schema:
                type: string
        '''   

        with rpc_proxy('say_wow_service') as rpc:
            say_result = rpc.say.call_async(text2say)  
            response = say_result.result() 
        # with ClusterRpcProxy(CONFIG) as rpc:
        #     # asynchronously spawning and email notification
        #     rpc.local_time_service.local.call_async()
        #     # asynchronously spawning the compute task
        #     say_result = rpc.say_wow_service.say.call_async(text2say)
        #     response = say_result.result()
        return {"text2say": response}, 200 


class Time(Resource):
    
    @marshal_with(time_fields)
    def get(self):
        with ClusterRpcProxy(CONFIG) as rpc:
            time_result = rpc.local_time_service.local.call_async()
            response = time_result.result()
        return {"time": response}, 200 

class Async(Resource):

    @marshal_with(time_fields)
    def get(self):
        with ClusterRpcProxy(CONFIG) as rpc:
            time_result = rpc.local_time_service.local()
            response = time_result.result()
        return {"time": "Action executed"}, 200 


class TimePg(Resource):
    
    # @marshal_with(arrange_fields)
    def get(self, timetext="Time Pg"):
        with rpc_proxy('db_time_service') as rpc:
            time = rpc.db()

        return time