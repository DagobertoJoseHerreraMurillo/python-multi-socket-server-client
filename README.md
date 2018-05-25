# python-multi-socket-server-client

Hello world!

# How to deploy lambda
First we need to create a user. We log in and go to IAM. Create a user
and set the "Programatic access". Then we create a group and attatch
the policy "AWSLambdaFullAccess".

Once the user is created, we create a role attatching the same
policy. Copy the role name for the future.

Go to the terminal and execute "aws configure". Enter your 
credentials. WHen it asks for the "default output", write "text"

Once your lambda is created, zip the content. Then execute:

```'aws lambda create-function --function-name "<your_function_name>" --runtime "python3.6" --role "<RoleName, example: arn:aws:iam::902263758114:role/service-role/RoleLambda>" --handler "<handler location (the start function), example: borrar/Main.lambda_handler>" --timeout <timeout_integer_in_seconds> --zip-file "fileb://./<YOUR_ZIP_FILE.zip" --region "<YOUR_REGION>eu-west-1"``` 

