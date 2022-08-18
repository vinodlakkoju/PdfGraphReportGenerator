import os
import json
import boto3
from PdfGenerator import PdfGenerator
import Constants as cons


def upload_to_s3(local_file, s3_file):
    s3 = boto3.client('s3')
    bucket = 'airaorig'
    try:
        s3.upload_file(local_file, bucket, s3_file)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket,
                'Key': s3_file
            },
            ExpiresIn=24 * 3600
        )

        print("Upload Successful", url)
        return url
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None


def handler(event, context):
    payload = json.loads(event['queryStringParameters']['payload'])
    print(f'Payload Type: {type(payload)}')
    print(payload)
    print('Generating pdf file')
    gen_pdf = PdfGenerator(payload)
    print('PDF object created')
    pdf_file = gen_pdf.createPages()
    # pdf_file = cons.COMPETENCY_BG_IMAGE
    print(f'PDF file path: {pdf_file}')

    s3_url = upload_to_s3(pdf_file, os.path.basename(pdf_file))
    print(f'S3 url: {s3_url}')
    return {
        'statusCode': 200,
        'body': json.dumps({'Report': s3_url})
        # 'body': json.dumps(payload)
    }
