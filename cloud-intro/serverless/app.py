from chalice import Chalice

app = Chalice(app_name='chalice-serverless')


@app.route('/', cors=True)
def index():
    return {'hello': 'world'}


@app.route('/uncertainty', cors=True)
def index():
    return {
                "Is this a JSON Object?": "I'm not sure",
                "Let's test it out!": "Ok",
                "It sure seems like it": "Yeah it seems to be...",
                "Let's join HCS to find out!": "Sounds like a plan!",
                "Creds to": "Eric Hansen"
            }
