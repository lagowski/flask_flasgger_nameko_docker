from flask_restful import Resource, fields, marshal_with, reqparse, abort

# what we expect
parser = reqparse.RequestParser()
parser.add_argument('text2show', required=True)
parser.add_argument('name')
parser.add_argument('simulate_error')


# what we return
resource_fields = {
    'data': fields.String,
}

def abort_if_simulate_error(simulate_error):
    if simulate_error:
         abort(404, message="Huston we have a problem :-)")

class Service1(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def post(self):
        args = parser.parse_args()
        response = {'data': args}
        abort_if_simulate_error(args['simulate_error'])
        return response

