#!/usr/bin/env python
import sys, getopt
import pandas as pd
import datetime


def read_csv(file_path, index_col_name, value_col_name ):

    cols =[index_col_name,value_col_name]
    #read data from csv input files with col name applied
    df = pd.read_csv(file_path, header=None, names=cols)

    #convert the string into timestamp datatype
    df[index_col_name] = pd.to_datetime(df[index_col_name], format='%Y-%m-%dT%H:%M:%S')

    return df

#print out result 
def print_result(df, col1, col2 ):
    for index, row in df.iterrows():
        idx = str(row[col1])
        value = row[col2]
        print('{idx} {value}'.format(idx=idx, value=value))

# To Question 1:
def sum_count(df, col_name):
    try:
        sum = df[col_name].sum()
        print(sum)
    except:
        print("An exception occurred when calculating sum of cars seen")


# To Question 2:
def sum_per_day(df, col_time, col_count):
    try:
        #convert the timeframe to date and get the count aggregated
        sum_per_day = df.groupby(df[col_time].dt.date)[col_count].agg('sum').reset_index()
        print_result(sum_per_day, col_time, col_count)
    except:
        print("An exception occurred when calculating sum of cars per day ")

# To Question 3:
def top3_half_hrs(df, col_time, col_count):
    try:
        #sort the value and select the top 3
        top3_half_hrs = df.sort_values(col_count,ascending = False).head(3) 
        print_result(top3_half_hrs, col_time, col_count )
    except:
       print("An exception occurred when calculating top3 half hours ")

# To Question 4:
def period_with_least_cars(df,index_col_name):
    #getting the rolling sum for the 3 contiguous half hour records
    if df.shape[0] > 2:
        try:
            #sort the dataframe based on timestamp to ensure the contiguity
            df = df.sort_values(by=index_col_name, ascending=True)

            #calculate the rolling sum for the past 3 half of hour period
            df['rolling_sum'] =df.rolling(3).sum()

            #get the starting timestamp for each period 
            df['starting_timestamp']= df[index_col_name].apply(lambda x: x - datetime.timedelta(minutes=90))

            #sort by rolling_sum and get the 1.5 hour period with least cars
            period_with_least_cars = df.sort_values('rolling_sum',ascending = True).head(1) 
            print('The 1.5 hour period after the below times with least cars' )
            print_result(period_with_least_cars, 'starting_timestamp', 'rolling_sum' )
        except:
            print("An exception occurred when calculating period with least cars ")
    else:
        print ("not enough records to calture the 1.5 hour period")


# main function to start the process
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h:f:p:i:v")
    except getopt.GetoptError as err:
        print(err)
        print('main.py -f <function> -p <file_path> -i <index_col_name> -v <value_col_name>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -f <function> -f <file_path> -i <index_col_name> -v <value_col_name>')
            sys.exit()
        elif opt in ("-f"):
            function = arg
        elif opt in ("-p"):
            file_path = arg    
        elif opt in ("-i"):
            index_col_name = arg    
        elif opt in ("-v"):
            value_col_name = arg    

    df = read_csv(file_path,index_col_name, value_col_name)
    
    #verify the datatype of input parameters
    if not df.empty:
        
        #execute the corresponding function
        if function == 'sum_count':
            sum_count(df, value_col_name)
        elif function == 'sum_per_day':
            sum_per_day(df, index_col_name, value_col_name)
        elif function == 'top3_half_hrs':
            top3_half_hrs(df, index_col_name, value_col_name)
        elif function == 'period_with_least_cars':
            period_with_least_cars(df, index_col_name)
        else:
            print ("please entour correct funtion names :" + '\n' 
            + '1. sum_count' + '\n' 
            + '2. sum_per_day' + '\n' 
            + '3. top3_half_hrs' + '\n'
            + '4. period_with_least_cars' + '\n')

    else:
        print("the input file is empty")