### Latency comparison of serverless computing between IBM Openwhisk and AWS Lambda


#### AWS Lambda
![alt text](https://github.com/satyamsah/compare-Serverless-Technologies/blob/master/lambdaflow.PNG)


1) As per the use case I created a trigger from AWS DynamoDB to call AWS Lambda

2) The AWS Lambda the call the lambda function to execute.

3) In this scenario I had tested noted down the timestamp of start of the execution of a program that pushes the data two the remote LAMBDA function. 
4) Latency: It is the time an application takes to be on wire. That mean from the time the application is triggered from the clients' environemnt(whether UI / or / code) till the application ends

5) I have take 5 test cases with input size. The input for each recods remains in simimar format.The data in the database in getting feeded in based on the number of iteration. The number of rows in the table is equal to the number of iterations. Each test case  depicts the latency when the data was transferred from clients' code to update in AWS  Dyanamodb database to triggering the AWS Lambda fucntion.

| number of records inserted in DB | time taken to execute the whole process(in second)|
| ------ | ------ |
| 500   | 1.7 seconds
| 1000  | 29.04 seconds
| 2500  | 05 min 47.776 seconds
| 5000 |  12 mins 38.903 seconds
| 10000 | 26 mins 33.789 seconds


#### IBM Openwhisk
![alt text](https://github.com/satyamsah/compare-Serverless-Technologies/blob/master/openwhiskflow.PNG)


1) As per the use case I created a trigger from IBM Cloudant to call IBM Openwhisk

2) The IBM Openwhisk the the lambda function to execute.

3) In this scenario I had tested noted down the timestamp of start of the execution of a program that pushes the data two the remote Openwhisk function. 
4) Latency: It is the time an application takes to be on wire. That mean from the time the application is triggered from the clients' environemnt(whether UI / or / code) till the application ends

5) I have take 5 test cases with input size. The input for each recods remains in simimar format.The data in the database in getting feeded in based on the number of iteration. The number of rows in the table is equal to the number of iterations. Each test case  depicts the latency when the data was transferred from clients' code to update in IBM cloudant database to triggering the IBM Openwhisk fucntion.

| number of records inserted in DB | time taken to execute the whole process(in seconds)|
| ------ | ------ |
| 500   | 20.7 seconds
| 1000  | 1 min 4.675 seconds
| 2500  | 04 min 67.569 seconds
| 5000 |  11 mins 35.656 seconds
| 10000 | 30 mins 23.005 seconds



### AWS Lambda Vs IBM Openwhisk

Below is the graph comaprison.As per the chart we can see that IBM Openwhisk-cloudant combination is swift when it comes to small data but AWS lambda-dynamodb combination experice less latency when it comes to high amount of data:

![alt text](https://github.com/satyamsah/compare-Serverless-Technologies/blob/master/Capture.PNG)
