
#### Create a function
aws lambda create-function --region us-east-2 --function-name ProcessDynamoDBStream2 --zip-file fileb://file-path/ProcessDynamoDBStream.zip --role XXXXXXXX --handler ProcessDynamoDBStream2.lambda_handler --runtime nodejs6.10

####creating a simulation of payload inspite of triggering from Lambda

aws lambda invoke --invocation-type RequestResponse --function-name ProcessDynamoDBStream --region us-east-1 --payload file://file-path/input.txt --profile adminuser outputfile.txt


#### Add an Event Source in AWS Lambda
aws lambda create-event-source-mapping --region us-east-2 --function-name ProcessDynamoDBStream2 --event-source XXXXXXX --batch-size 100 --starting-position TRIM_HORIZON


##### List the event sources in AWS Lambda
aws lambda list-event-source-mappings --region us-east-2 --function-name ProcessDynamoDBStream2 --event-source XXXXXXXX