CREATE SCHEMA IF NOT EXISTS "carcrash";

CREATE  TABLE "carcrash".dim_contributingfactors ( 
	contributingfactor_id BIGINT  NOT NULL  ,
	contributing_factor  VARCHAR(255)    ,
	CONSTRAINT pk_dim_contributingfactors PRIMARY KEY ( contributingfactor_id )
 );

CREATE  TABLE "carcrash".dim_date ( 
	date_id              BIGINT  NOT NULL  ,
	date_iso_format      DATETIME    ,
	year_number          INT    ,
	quarter_number       INT    ,
	month_number         INT    ,
	month_name           VARCHAR(50)    ,
	day_number           INT    ,
	day_name             VARCHAR(50)    ,
	hour_number          INT    ,
	week_of_month        INT    ,
	week_of_year         INT    ,
	CONSTRAINT pk_dim_date PRIMARY KEY ( date_id )
 );

CREATE  TABLE "carcrash".dim_location ( 
	location_id          BIGINT  NOT NULL  ,
	borough              VARCHAR(255)    ,
	latitude             DOUBLE    ,
	longitude            DOUBLE    ,
	zip_code             INT    ,
	on_street_name       VARCHAR(255)    ,
	off_street_name      VARCHAR(255)    ,
	CONSTRAINT pk_dim_location PRIMARY KEY ( location_id )
 );

CREATE  TABLE "carcrash".dim_vehicle_type ( 
	vehicle_id           BIGINT  NOT NULL  ,
	vehicle_type_code    VARCHAR(255)    ,
	CONSTRAINT pk_dim_vehicle_type PRIMARY KEY ( vehicle_id )
 );

CREATE  TABLE "carcrash".facts_crashes ( 
	fact_id              BIGINT  NOT NULL  ,
	number_of_persons_injured INT    ,
	number_of_persons_killed INT    ,
	number_of_pedestrians_injured INT    ,
	number_of_pedestrians_killed INT    ,
	number_of_cyclist_injured INT    ,
	number_of_cyclist_killed INT    ,
	number_of_motorist_injured INT    ,
	number_of_motorist_killed INT    ,
	location_id          INT    ,
	date_id              BIGINT    ,
	vahicle_id           INT    ,
	contributing_factor_id INT    ,
	CONSTRAINT pk_facts_crashes PRIMARY KEY ( fact_id )
 );
