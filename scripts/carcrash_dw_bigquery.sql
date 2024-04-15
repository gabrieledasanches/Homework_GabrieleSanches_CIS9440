CREATE SCHEMA INSTANCE;

CREATE TABLE carcrash_dw_lgl.INSTANCE.dim_contributingfactors ( 
	contributingfactor_id int64 NOT NULL  ,
	contributing_factor string  
 );

ALTER TABLE carcrash_dw_lgl.INSTANCE.dim_contributingfactors ADD PRIMARY KEY ( contributingfactor_id )  NOT ENFORCED;

CREATE TABLE carcrash_dw_lgl.INSTANCE.dim_date ( 
	date_id int64 NOT NULL  ,
	year int64  ,
	monthNumber int64  ,
	quarter int64  ,
	dayNumber int64  ,
	dayName string  ,
	monthName string  ,
	week_of_the_month int64  ,
	week_of_the_year int64  ,
	hourNumber int64  ,
	date_isoformat datetime  
 );

ALTER TABLE carcrash_dw_lgl.INSTANCE.dim_date ADD PRIMARY KEY ( date_id )  NOT ENFORCED;

CREATE TABLE carcrash_dw_lgl.INSTANCE.dim_location ( 
	location_id int64 NOT NULL  ,
	borough string  ,
	latitude bignumeric  ,
	longitude bignumeric  ,
	zip_code int64  ,
	on_street_name string  ,
	off_street_name string  ,
	cross_street_name string  
 );

ALTER TABLE carcrash_dw_lgl.INSTANCE.dim_location ADD PRIMARY KEY ( location_id )  NOT ENFORCED;

CREATE TABLE carcrash_dw_lgl.INSTANCE.dim_vehicle_type ( 
	vehicle_id int64 NOT NULL  ,
	vehicle_type_code string  
 );

ALTER TABLE carcrash_dw_lgl.INSTANCE.dim_vehicle_type ADD PRIMARY KEY ( vehicle_id )  NOT ENFORCED;

CREATE TABLE carcrash_dw_lgl.INSTANCE.facts_crashes ( 
	fact_id int64 NOT NULL  ,
	number_of_persons_injured int64  ,
	number_of_persons_killed int64  ,
	number_of_pedestrians_injured int64  ,
	number_of_pedestrians_killed int64  ,
	number_of_cyclist_injured int64  ,
	number_of_cyclist_killed int64  ,
	number_of_motorist_injured int64  ,
	number_of_motorist_killed int64  ,
	number_of_accidents int64  ,
	location_id int64  ,
	date_id int64  ,
	vahicle_id int64  ,
	contributing_factor_id int64  
 );

ALTER TABLE carcrash_dw_lgl.INSTANCE.facts_crashes ADD PRIMARY KEY ( fact_id )  NOT ENFORCED;
