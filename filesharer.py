from filestack import Client

class FileSharer:
    #api
    #file_path
    def __init__(self, file_path, api_key='AtSg9zKMTb2ip0XyxUVNcz'):
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.file_path)
        return new_file_link.url    













