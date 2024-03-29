# Analyzes text in a document stored in an S3 bucket. Display polygon box around text and angled text
import boto3
from flask import Flask
import os
from dotenv import load_dotenv
from text_extract import process_text_analysis
load_dotenv()

session = boto3.Session(
    os.getenv("AWS_KEY_ID"),
    os.getenv("AWS_SECRET_ACCESS_KEY")
)
s3_connection = session.resource('s3')
client = session.client('textract',
                        region_name=os.getenv("AWS_DEFAULT_REGION"))

app = Flask(__name__)

@app.route('/')
def main():
    bucket = "document-analysis-api"
    document = "document_analysis_test_1.png"
    block_info = process_text_analysis(s3_connection, client, bucket, document)
    return {
        "Blocks detected": block_info
    }


if __name__ == '__main__':
    app.run(debug=True)
