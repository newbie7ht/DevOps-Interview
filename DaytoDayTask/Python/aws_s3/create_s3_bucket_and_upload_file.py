import boto3

s3 = boto3.client('s3')

bucket_name = "my-devops-bucket"
file_name = "example.txt"
file_content = "Hello, this is a test file."

# Create an S3 bucket
s3.create_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' created.")

# Upload a file to the bucket
s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
print(f"File '{file_name}' uploaded to bucket '{bucket_name}'.")


'''
2. Set Expiration on S3 Objects
You can set a lifecycle policy on the S3 bucket to automatically delete objects after 24 hours.

S3 Lifecycle Policy JSON:

json
Copy code
{
    "Rules": [
        {
            "ID": "DeleteLogsAfter24Hours",
            "Prefix": "logs/",
            "Status": "Enabled",
            "Expiration": {
                "Days": 1
            }
        }
    ]
}
Steps to Apply the Policy:

Go to the S3 Console:

Navigate to the S3 bucket where the logs are stored.
Set Up Lifecycle Rules:

Go to the "Management" tab in your S3 bucket.
Click "Create lifecycle rule."
Give the rule a name, e.g., DeleteLogsAfter24Hours.
Under "Rule scope," select "Apply to all objects in the bucket" or specify a prefix like logs/.
In the "Lifecycle rule actions," select "Expire current versions of objects" and set it to 1 day.
Save the rule.
Explanation:

This lifecycle policy automatically deletes objects in the S3 bucket that are older than 24 hours (1 day).
Putting It All Together:
Run the Python Script to upload the logs to the S3 bucket. This script can be scheduled to run at regular intervals (e.g., hourly, daily) using a cron job.
The Lifecycle Policy on the S3 bucket will take care of deleting the logs after 24 hours automatically.
How to Present This in an Interview:
You could say:

"In a scenario where I need to copy logs from a local directory to an S3 bucket and then delete them after 24 hours, 
I would write a Python script using boto3 to automate the upload process. I’d then apply a lifecycle policy directly in S3 to handle the deletion automatically after 24 hours. 
This ensures that the logs are stored securely and managed efficiently without requiring manual intervention."

'''