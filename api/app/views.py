from flask import render_template, request
from app import app
from cassandra.cluster import Cluster

# connect to cassandra database
cluster = Cluster(<ip-address>)
session = cluster.connect(<the keyspace in the cassandra to connect>)

@app.route('/api/authorization', methods=['GET'])
def authorize():
    # create a new token in the authentication_token table
    pass

# demo web page
@app.route("/api/users/<user_id>/<mood>", , methods=['POST'])
def upload(user_id, mood):
    # Authentication
    authenticate(request.form["authentication"])
    
    # validate user_id, mood, and location
    latitude, lontitude = request.form["location"]
    # insert
    return

# take GET request from bar2.html and return the data to display
@app.route('/api/users/<user_id>/moods', methods=['GET'])
def moodsDistribution(user_id):
    # Authentication
    authenticate(request.form["authentication"])
    
    # validate user_id
    
    # get the count of  group by mood
    query = "SELECT COUNT(*) FROM mood_fact WHERE user_id = '%s' GROUP BY mood_id" % (user_id)
    response = session.execute(query)
    pass
    
@app.route('/api/users/<user_id>/proximity', methods=['GET'])
def getProxmity(user_id):
    # Authentication
    authenticate(request.form["authentication"])
    # validate user_id
    
    # return the nearest location if the user is happy within one hour.
    pass

def authenticate(token):
    # query authentication_token table and check if the token is authorized
    pass