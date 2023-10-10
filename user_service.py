import boto3
from botocore.exceptions import ClientError
from uuid import uuid4

class UserService():
    def __init__(self, table):
        self.table = boto3.resource("dynamodb").Table(table)

    def create_user(self, user_data):

        # Scenario 1: User id is created since user id is not expected
        # user_data["id"] = str(uuid4())

        # Scenario 2: User id is expected

        if not "id" in list(user_data.keys()):
            return {"error": "id is required"}
    
        try:
            response = self.table.put_item(Item=user_data)
            return {'status': 200, "user_id" : user_data["id"]}
        except ClientError as e:
            return {'error': str(e)}        
    
    def get_user_by_id(self, user_id):
        try:
            response = self.table.get_item(Key={'id': str(user_id)})
            user = response.get('Item')
            if user:
                return {'user': user}
            else:
                return {'message': 'User not found'}
        except ClientError as e:
            return {'error': str(e)}