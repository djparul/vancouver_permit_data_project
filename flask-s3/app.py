from flask import Flask, request, jsonify
app = Flask(__name__) # creates the Flask instance
import boto3
# from botocore.config import Config
from config import S3_BUCKET, S3_KEY, S3_SECRET
from cloudwatch_helper import *

# Decorate a view function to register it with the given URL rule and options.
@app.route("/s3", methods = ['GET'])
def get():
    s3 = boto3.client(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key = S3_SECRET
)
    # Call S3 to list current buckets
    response = s3.list_buckets()
    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    # Print out the bucket list
    return ("Bucket List: %s" % buckets)
 
@app.route("/s3", methods = ['POST'])
def create():
    s3 = boto3.client(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key = S3_SECRET
)
    cw_metric = cloudwatch_metric('CreateBucketSuccess', 'Count')
    
    bucket = request.get_json() # Parses the incoming JSON request data and returns it
    s3.create_bucket(Bucket=bucket['name'])
    try:
        print("cloudwatch_response" + cw_metric)
    finally:
        return ("The bucket has been created on s3 named : " + bucket['name'])

@app.route("/s3/<string:old_bucket_name>/<string:new_bucket_name>", methods = ['PUT'])
def update(old_bucket_name, new_bucket_name):
    
    return ("Renaming a bucket is not allowed")
@app.route("/s3/<string:bucket_name>", methods = ['DELETE'])
def delete(bucket_name):
    s3 = boto3.client(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key = S3_SECRET
)
    s3.delete_bucket(Bucket=bucket_name)
    return (bucket_name + "has been deleted")

if __name__ == '__main__':
    app.run(debug =  True, port=5000)