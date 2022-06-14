from minio import Minio
from minio.error import S3Error

client = Minio("144.91.70.164:9000", access_key="ROOT1234", secret_key="ROOT1234", secure=False)

if __name__ == '__main__':
    try:
        picture_bucket = client.bucket_exists('picture')
        if picture_bucket:
            print("picture_bucket existe")

    except Exception as e:
        print(e)


