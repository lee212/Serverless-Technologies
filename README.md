### Latency comparison of serverless computing between IBM Openwhisk and AWS Lambda


#### AWS Lambda
![alt text](https://github.com/satyamsah/compare-Serverless-Technologies/blob/master/lambdaflow.PNG)


1) As per the use case I created a trigger from AWS DynamoDB to call AWS Lambda

2) The AWS Lambda the call the lambda function to execute.

3) In this scenario I had tested noted down the timestamp of start of the execution of a program that pushes the data two the remote LAMBDA function. 
4) Latency: It is the time an application takes to be on wire. That mean from the time the application is triggered from the clients' environemnt(whether UI / or / code) till the application ends

5) I have take 5 test cases with input size. The input for each recods remains in simimar format.The data in the database in getting feeded in based on the number of iteration. The number of rows in the table is equal to the number of iterations. Each tet case also depicts the time to generate the code.

| number of iterations | time inteval to execute(in seconds|
| ------ | ------ |
| 500   | 70.69
| 1000  | 100.69 
| 2000  | 170.33
| 10000 | 748.73


#### IBM Openwhisk
![alt text](https://github.com/satyamsah/compare-Serverless-Technologies/blob/master/openwhiskflow.PNG)


1) As per the use case I created a trigger from IBM Cloudant to call IBM Openwhisk

2) The IBM Openwhisk the the lambda function to execute.

3) In this scenario I had tested noted down the timestamp of start of the execution of a program that pushes the data two the remote Openwhisk function. 
4) Latency: It is the time an application takes to be on wire. That mean from the time the application is triggered from the clients' environemnt(whether UI / or / code) till the application ends

5) I have take 5 test cases with input size. The input for each recods remains in simimar format.The data in the database in getting feeded in based on the number of iteration. The number of rows in the table is equal to the number of iterations. Each tet case also depicts the time to generate the code.

| number of iterations | time inteval to execute(in seconds|
| ------ | ------ |
| 500   | 70.69
| 1000  | 100.69 
| 2000  | 170.33
| 10000 | 748.73






