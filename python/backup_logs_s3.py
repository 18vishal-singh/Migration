# import boto3
# from botocore.exceptions import ClientError
# import os
# from datetime import datetime, timedelta
# import schedule
# import time
#
# def upload_file_to_s3(file_name, bucket, object_name=None, folder_name=None):
#     """
#     Upload a file to an S3 bucket.
#
#     Params:
#         file_name: File to upload
#         bucket: Bucket to upload to
#         object_name: S3 object name. If not specified then file_name is used
#         folder_name: Folder name in which file is to be uploaded
#     """
#
#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = file_name.split('/')[-1]
#         # If folder_name was specified, upload in the folder
#         if folder_name is not None:
#             object_name = f'{folder_name}/{object_name}'
#
#     # Upload the file
#     try:
#         s3_client = boto3.client(
#             service_name='s3',
#             aws_access_key_id='key',
#             aws_secret_access_key='secret'
#         )
#         response = s3_client.upload_file(file_name, bucket, object_name)
#         print(response)
#     except ClientError as e:
#         print(e)
#
#
# def append_text_to_file_names(files, text):
#     """
#     Appends given text to the name of the files.
#
#     Params:
#         files: List(str): list of file paths
#         text: str: Text that is to appended
#     Returns:
#         files: List(str): list of file paths with text appended
#     """
#     for i in range(len(files)):
#         file_splitted = files[i].split('/')
#         file_path = file_splitted[:-1]
#         file_name = file_splitted[-1]
#         file_name_splitted = file_name.split('.')
#         new_file_name = '.'.join([file_name_splitted[0], text, file_name_splitted[1]])
#         file_path.append(new_file_name)
#         new_file_name_with_path = '/'.join(file_path)
#         os.rename(files[i], new_file_name_with_path)
#         files[i] = new_file_name_with_path
#     return files
#
#
# def rename_and_backup_logs_s3():
#     """
#     Backsup log files to s3 bucket
#     """
#     today = datetime.now()
#     yesterday = today - timedelta(days=1)
#     text = yesterday.strftime('%d-%m-%Y')
#
#     log_files = [
#         '/Users/sivishal/VishalTestArea/log1.txt',
#         '/Users/sivishal/VishalTestArea/log2.txt'
#     ]
#
#     print('Appending date to log files...')
#     log_files = append_text_to_file_names(log_files, text)
#     print('Appended date to log files...')
#
#     print('Uploading logs to S3...')
#     for log_file in log_files:
#         upload_file_to_s3(
#             file_name=log_file,
#             bucket='sivishal-v2migration',
#             folder_name='test_logs'
#         )
#     print('Uploaded logs to S3...')
#
#
# if __name__ == "__main__":
#     rename_and_backup_logs_s3()