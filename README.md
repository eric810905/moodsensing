# Introduction
This is the skeleton code of the backend API for mood sensing application. The backend service is implemented by Flask. Cassandra is the choice for database. I use google places API to find the nearest location given user's location. (https://developers.google.com/places/web-service/)

## Assumptions
1. The mood data is very large and cannot be fit into a machine.
2. The third call API will return a nearest location (home, office, shopping center) if the given user is happy now. I assume the users are happy if the latest mood record in the database is happy and the timestamp is within one hour.

## Define API
upload a mood:
POST /api/users/<user_id>/<mood>
{"authentication": "XYZ", "location": {"lat": 33.3, "lon": 13.3}}

return the mood frequency:
GET /api/users/<user_id>/moods
{"authentication": "XYZ"}

return the proximity to a location:
GET /api/users/<user_id>/proximity
{"authentication": "XYZ"}

## Layout code structure
main files are:
1. app/views.py: the backend API service.
2. unittests.py: test the backend service.
3. cassandraTable.cql: create tables in cassandra cluster. Define the partition key.

## Design data model and key data structures
Three tables are stored in Cassandra. I choose NoSQL database because mood_fact table can potentially be very large. Cassandra can sort the records by time stamp, which is a advantage for proximity API.
1. mood_fact
    user_id(PK)
    date
    time
    mood_key(FK)

2. mood_dim
    mood_key(PK)
    mood

3. authentication_token
    token

## Unit tests
1. test the correctness
2. test the robustness (throughput)
3. test the latency
