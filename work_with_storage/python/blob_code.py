# coding: utf-8

import os
from azure.storage.blob import BlobServiceClient
class PythonBlobLab(object):

    # Hint: To make use of these variables in code, you need to prepend them with "self" like this: self.my_connection_string and self.source_file
    my_connection_string = ""
    source_file = "test.txt"

    def practice_operations(self):

        # Instantiate a BlobServiceClient using a connection string

        client = BlobServiceClient.from_connection_string(self.my_connection_string)
        #print(dir(client))
        print(client.get_account_information())
        

        # Instantiate a ContainerClient object and create the container.

        #my_container_client = client.create_container("containerforlab1")
        #print(my_container_client.name)

        container_client = client.get_container_client("containerforlab2")
        #print(dir(container_client))
        print(container_client.container_name, container_client.url)

        # Instantiate a new BlobClient object
        my_blob_client = container_client.get_blob_client(self.source_file)
        with open(self.source_file, "rb") as data:
            my_blob_client.upload_blob(data, blob_type="BlockBlob")

        
       

example=PythonBlobLab()
example.practice_operations()

