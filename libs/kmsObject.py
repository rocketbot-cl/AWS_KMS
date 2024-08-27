import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os
import base64

class kmsObject:
    def __init__(self, awsAccessKeyId, awsSecretAccessKey, regionName='us-west-2'):
        try:
            self.session = boto3.Session(aws_access_key_id=awsAccessKeyId, aws_secret_access_key=awsSecretAccessKey,
            region_name=regionName)
            #para comprobar que las credenciales son correctas:
            kms_client = self.session.client('kms', region_name=regionName)
            kms_client.list_keys()
        except ClientError as e:
            print(f"Error connecting to AWS KMS: {e}")
            raise ValueError("Invalid AWS credentials") from e
    def create_key(self, description='Default KMS Key'):
        try:
            kms = self.session.client('kms')
            response = kms.create_key(
                Description=description
            )
            return response['KeyMetadata']
        except ClientError as e:
            print(f"Error creating key: {e}")
            return None
        
    def encrypt(self, key_id, plaintext):
        try:
            kms = self.session.client('kms')
            response = kms.encrypt(
                KeyId=key_id,
                Plaintext=plaintext
            )
            ciphertext_blob = base64.b64encode(response['CiphertextBlob']).decode('utf-8')
            return ciphertext_blob
            # return response['CiphertextBlob']
        except (BotoCoreError, ClientError) as error:
            print(f"Error encrypting data: {error}")
            return None

    def decrypt(self, ciphertext_blob):
        try:
            kms = self.session.client('kms')
            ciphertext_blob = base64.b64decode(ciphertext_blob.encode('utf-8'))
            response = kms.decrypt(
                CiphertextBlob=ciphertext_blob
            )
            return response['Plaintext']
        except (BotoCoreError, ClientError) as error:
            print(f"Error decrypting data: {error}")
            return None

    def list_keys(self):
        try:
            kms = self.session.client('kms')
            keys = []
            response = kms.list_keys()
            keys.extend(response['Keys'])

            # paginación en caso de haber más claves
            while 'NextMarker' in response:
                response = kms.list_keys(Marker=response['NextMarker'])
                keys.extend(response['Keys'])

            # obtener descripciones de cada clave en caso de tenerla
            described_keys = []
            for key in keys:
                key_id = key['KeyId']
                try:
                    key_description = kms.describe_key(KeyId=key_id)
                    key_metadata = key_description['KeyMetadata']
                    described_keys.append({
                        'KeyId': key_metadata['KeyId'],
                        'Description': key_metadata.get('Description', 'No description available')
                    })
                except ClientError as e:
                    print(f"Error describing key {key_id}: {e}")
                    described_keys.append({
                        'KeyId': key_id,
                        'Description': 'Error retrieving description'
                    })

            return described_keys
        except ClientError as e:
            print(f"Error listing keys: {e}")
            return None

    def encrypt_file(self, key_id, input_file_path, output_file_path):
        try:
            with open(input_file_path, 'rb') as file:
                plaintext = file.read()
            encrypted_text = self.encrypt(key_id, plaintext)
            if encrypted_text:
                with open(output_file_path, 'wb') as file:
                    file.write(encrypted_text)
                return True
            return False
        except Exception as e:
            print(f"Error encrypting file: {e}")
            return False

    def decrypt_file(self, input_file_path, output_file_path):
        try:
            with open(input_file_path, 'rb') as file:
                ciphertext_blob = file.read()
            decrypted_text = self.decrypt(ciphertext_blob)
            if decrypted_text:
                with open(output_file_path, 'wb') as file:
                    file.write(decrypted_text)
                return True
            return False
        except Exception as e:
            print(f"Error decrypting file: {e}")
            return False