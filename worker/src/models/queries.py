table_trips = "trips"

table_vendor_lookup = 'vendor_lookup'

table_payment_lookup = 'payment_lookup'


table_trips_columns = "vendor_id varchar(255), pickup_datetime DATE, dropoff_datetime DATE, passenger_count INTEGER, trip_distance FLOAT,	pickup_longitude FLOAT,	pickup_latitude FLOAT, rate_code FLOAT, store_and_fwd_flag FLOAT, dropoff_longitude FLOAT, dropoff_latitude FLOAT, payment_type varchar(255), fare_amount FLOAT, surcharge FLOAT, tip_amount FLOAT, tolls_amount FLOAT, total_amount FLOAT"

table_vendor_lookup_columns = "vendor_id varchar(255), name varchar(255), address varchar(255), city varchar(255), state varchar(255), zip varchar(255), country varchar(255), contact varchar(255), current varchar(255)"

table_payment_lookup = "payment_type varchar(255), payment_lookup varchar(255)"


create_statement = """
        DROP TABLE IF EXISTS {};
        CREATE TABLE {}({});
		"""

insert_statement = """INSERT INTO {} ({}) VALUES %s"""

update_statement = """UPDATE {} SET payment_type = '{}' WHERE payment_type = '{}';"""


json_path = "./datasets"

vendor_path = "./datasets/data-vendor_lookup-csv.csv"

payment_path = "./datasets/data-payment_lookup-csv.csv"

##average distance in trips with max 2 passenger
avg_distance_2_passengers = """SELECT avg(trip_distance) FROM trips WHERE passenger_count < 3"""

### top 3 vendors by total_amount
top_vendors = """SELECT vendor_id, SUM(total_amount) FROM trips GROUP BY vendor_id ORDER BY SUM(total_amount) DESC LIMIT 3"""

## trips paid with money in all years
money_paid = """ select dropoff_datetime from trips where payment_type = 'Cash' """

##tips per day in the last 3 months of 2012
tips_per_day = """select dropoff_datetime, sum(tip_amount) from trips where dropoff_datetime >'2012-09-30' group by dropoff_datetime"""