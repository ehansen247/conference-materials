from chalice import Chalice

app = Chalice(app_name='chalice-serverless')


@app.route('/', cors=True)
def index():
    return {'hello': 'world'}


@app.route('/cool',cors=True)
def index():
    return {'which_endpoint_is_the_coolest?': 'this endpoint is the coolest !!!'}
