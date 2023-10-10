## Users api service
### Dependencies

Prerequisite to start deploying application is having python and npm installed.

### Deployment

In order to deploy application, install serverless framework

```
npm install -g serverless
```

install plugins:

```
serverless plugin install --name serverless-wsgi
serverless plugin install --name serverless-python-requirements
```

and then perform deployment with:

```
serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying users-api to stage dev (us-east-1)

✔ Service deployed to stack users-api-dev (123s)

endpoints:
  POST - https://<api-gateway-id>.execute-api.<aws-region>.amazonaws.com/dev/users
  GET - https://<api-gateway-id>.execute-api.<aws-region>.amazonaws.com/dev/users/{user_id}
functions:
  create-user: users-api-dev-create-user (1.8 MB)
  get-user: users-api-dev-get-user (1.8 MB)
```

### Invocation

After successful deployment, you can create a new user by calling the corresponding endpoint:

```bash
curl --request POST 'https://<api-gateway-id>.execute-api.<aws-region>.amazonaws.com/users' --header 'Content-Type: application/json' --data-raw '{"name": "John", "email": "johndoe@gmail.com","id": "someUserId"}'
```

Which should result in the following response:

```bash
{"status": 200, "user_id" : "someUserId"}
```

You can later retrieve the user by `userId` by calling the following endpoint:

```bash
curl https://<api-gateway-id>.execute-api.<aws-region>.amazonaws.com/users/someUserId
```

Which should result in the following response:

```bash
{ "user": { "email": "johndoe@gmail.com", "id": "someUserId", "name": "John"} }
```

If you try to retrieve user that does not exist, you should receive the following response:

```bash
{"error":"id is required"}
```

