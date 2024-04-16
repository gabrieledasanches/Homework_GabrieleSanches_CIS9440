CREATE SCHEMA IF NOT EXISTS "instance";

CREATE  TABLE "instance".dim_contributingfactors ( 
	contributingfactor_id BIGINT  NOT NULL  ,
	contributing_factor  VARCHAR(255)    ,
	CONSTRAINT pk_dim_contributingfactors PRIMARY KEY ( contributingfactor_id )
 );

CREATE  TABLE "instance".dim_date ( 
	date_id              BIGINT  NOT NULL  ,
	"year"               INT    ,
	monthnumber          INT    ,
	quarter              INT    ,
	daynumber            INT    ,
	dayname              VARCHAR(50)    ,
	monthname            VARCHAR(50)    ,
	week_of_the_month    INT    ,
	week_of_the_year     INT    ,
	hournumber           INT    ,
	date_isoformat       DATETIME    ,
	CONSTRAINT pk_dim_date PRIMARY KEY ( date_id )
 );

CREATE  TABLE "instance".dim_location ( 
	location_id          BIGINT  NOT NULL  ,
	borough              VARCHAR(255)    ,
	latitude             DOUBLE    ,
	longitude            DOUBLE    ,
	zip_code             INT    ,
	on_street_name       VARCHAR(255)    ,
	off_street_name      VARCHAR(255)    ,
	cross_street_name    VARCHAR(255)    ,
	CONSTRAINT pk_dim_location PRIMARY KEY ( location_id )
 );

CREATE  TABLE "instance".dim_vehicle_type ( 
	vehicle_id           BIGINT  NOT NULL  ,
	vehicle_type_code    VARCHAR(255)    ,
	CONSTRAINT pk_dim_vehicle_type PRIMARY KEY ( vehicle_id )
 );

CREATE  TABLE "instance".facts_crashes ( 
	fact_id              BIGINT  NOT NULL  ,
	number_of_persons_injured INT    ,
	number_of_persons_killed INT    ,
	number_of_pedestrians_injured INT    ,
	number_of_pedestrians_killed INT    ,
	number_of_cyclist_injured INT    ,
	number_of_cyclist_killed INT    ,
	number_of_motorist_injured INT    ,
	number_of_motorist_killed INT    ,
	number_of_accidents  INT    ,
	location_id          INT    ,
	date_id              BIGINT    ,
	vahicle_id           INT    ,
	contributing_factor_id INT    ,
	CONSTRAINT pk_facts_crashes PRIMARY KEY ( fact_id )
 );
