CREATE SCHEMA CARCRASH;

CREATE  TABLE "carcrash_dw_lgl".CARCRASH.DIM_CONTRIBUTINGFACTORS ( 
	CONTRIBUTINGFACTOR_ID integer NOT NULL   ,
	CONTRIBUTING_FACTOR  varchar(255)    ,
	CONSTRAINT PK_DIM_CONTRIBUTINGFACTORS PRIMARY KEY ( CONTRIBUTINGFACTOR_ID )
 );

CREATE  TABLE "carcrash_dw_lgl".CARCRASH.DIM_DATE ( 
	DATE_ID              integer NOT NULL   ,
	DATE_ISO_FORMAT      datetime    ,
	YEAR_NUMBER          integer    ,
	QUARTER_NUMBER       integer    ,
	MONTH_NUMBER         integer    ,
	MONTH_NAME           varchar(50)    ,
	DAY_NUMBER           integer    ,
	DAY_NAME             varchar(50)    ,
	HOUR_NUMBER          integer    ,
	WEEK_OF_MONTH        integer    ,
	WEEK_OF_YEAR         integer    ,
	CONSTRAINT PK_DIM_DATE PRIMARY KEY ( DATE_ID )
 );

CREATE  TABLE "carcrash_dw_lgl".CARCRASH.DIM_LOCATION ( 
	LOCATION_ID          integer NOT NULL   ,
	BOROUGH              varchar(255)    ,
	LATITUDE             double    ,
	LONGITUDE            double    ,
	ZIP_CODE             integer    ,
	ON_STREET_NAME       varchar(255)    ,
	OFF_STREET_NAME      varchar(255)    ,
	CONSTRAINT PK_DIM_LOCATION PRIMARY KEY ( LOCATION_ID )
 );

CREATE  TABLE "carcrash_dw_lgl".CARCRASH.DIM_VEHICLE_TYPE ( 
	VEHICLE_ID           integer NOT NULL   ,
	VEHICLE_TYPE_CODE    varchar(255)    ,
	CONSTRAINT PK_DIM_VEHICLE_TYPE PRIMARY KEY ( VEHICLE_ID )
 );

CREATE  TABLE "carcrash_dw_lgl".CARCRASH.FACTS_CRASHES ( 
	FACT_ID              integer NOT NULL   ,
	NUMBER_OF_PERSONS_INJURED integer    ,
	NUMBER_OF_PERSONS_KILLED integer    ,
	NUMBER_OF_PEDESTRIANS_INJURED integer    ,
	NUMBER_OF_PEDESTRIANS_KILLED integer    ,
	NUMBER_OF_CYCLIST_INJURED integer    ,
	NUMBER_OF_CYCLIST_KILLED integer    ,
	NUMBER_OF_MOTORIST_INJURED integer    ,
	NUMBER_OF_MOTORIST_KILLED integer    ,
	LOCATION_ID          integer    ,
	DATE_ID              integer    ,
	VAHICLE_ID           integer    ,
	CONTRIBUTING_FACTOR_ID integer    ,
	CONSTRAINT PK_FACTS_CRASHES PRIMARY KEY ( FACT_ID )
 );
