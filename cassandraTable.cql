CREATE TABLE mood_fact (user_id text, date text, time timestamp, mood_key text, PRIMARY KEY ((user_id, date), time), ) WITH CLUSTERING ORDER BY (time DESC);
CREATE TABLE mood_dim (mood_id text, mood text, PRIMARY KEY ((mood_id), ));
