# Traffic Counter Code Challenge

## About the Project

Write a program that reads a file, where each line contains a timestamp (in yyyy-mm ddThh:mm:ss format, i.e. ISO 8601) for the beginning of a half-hour and the number of  cars seen that half hour. An example file please see below.  

<br />

> Input file examle:
>
>2021-12-01T05:00:00 12 \
>2021-12-01T06:00:00 14 \
>2021-12-01T06:30:00 15 

<br />

## Aussumption

- clean input  can be expected as it's machine-generated.
- input file format .csv

<br />

## Prerequisites

- python version: Python 3.9.7
- python modules:
  - sys
  - pandas
  - getopt
  - datetime

<br />

## Quick Start

- Clone this repo using git clone 
- Move to the appropriate directory: 
    > cd traffic_counter/main.
- Run command line:
  
  > python main.py -f <function_name> -p <file_path> -i <index_col_name> -v <count_col_name>


### Note: 
- use -p to indicate file path
- use -i to indicate the index column name , eg. timestamp
- use -v to indicate the column name of the value, eg. count
- use -f to indicate the function to each question :
  - **sum_count** -> print out the number of cars seen in total
  - **sum_per_day** -> A sequence of lines where each line contains a date (in yyyy-mm-dd format) and the  number of cars seen on that day (eg. 2016-11-23 289) for all days listed in the input file
  - **top3_half_hrs** -> list the top 3 half hours with most cars.
  - **period_with_least_cars** -> The 1.5 hour period with least cars

  <br />
- example:
    > python main.py -f sum_per_day -p ../traffic_counter.csv -i timestamp -v count

<br />


## Unit Test
 
- Move to the unit test directory: 
    > cd ../unittest
- Run command line:
  
  > python test_main.py

<br />

## Future Work

- Imagine the file exported to S3, a boto3 connection needs to be added on, or other connectors to other platforms.

- data warehouse can be utilised via SQL to enable quicker data manipulation than using pandas.

- RESTful API can create a better user experience 
