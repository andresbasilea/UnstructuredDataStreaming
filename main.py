from pyspark.sql import SparkSession

from config import configuration

if __name__ == "__main__":
    spark = (SparkSession.builder.appName('UnstructuredDataStreaming')
             .config('spark.jars.packages',
                     'org.apache.hadoop:hadoop-aws:3.3.1,'
                     'com.amazonaws:aws-java-sdk:1.11.469'
                     )
            .config('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
            .config('spark.hadoop.fs.s3a.access.key', configuration.get('AWS_ACCESS_KEY'))
            .config('spark.hadoop.fs.s3a.secret.key', configuration.get('AWS_SECRET_KEY'))
            .config('spark.hadoop.fs.s3a.aws.credentials.provider',
                     'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')

            .getOrCreate())
    

    text_input_dir = 'file:///home/andres/Documents/DataEngineeringML/ProjectUnstructuredDataStreaming/input/input_text'
    json_input_dir = 'file:///home/andres/Documents/DataEngineeringML/ProjectUnstructuredDataStreaming/input/input_json'
    csv_input_dir = '/home/andres/Documents/DataEngineeringML/ProjectUnstructuredDataStreaming/input/input_csv'
    pdf_input_dir = '/home/andres/Documents/DataEngineeringML/ProjectUnstructuredDataStreaming/input/input_pdf'
    video_input_dir = '/home/andres/Documents/DataEngineeringML/ProjectUnstructuredDataStreaming/input/input_video'

    