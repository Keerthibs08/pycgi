#!C:\Users\Keerthi\AppData\Local\Programs\Python\Python38-32\python.exe
import boto3
import json
import decimal
import pymsgbox
import cgi,cgitb
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

print("Content-type: text/html\r\n\r\n")

form=cgi.FieldStorage()

username=form.getvalue("username")
password=form.getvalue("password")

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                return str(o)
            return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb',region_name='us-east-2',
    aws_access_key_id='',
    aws_secret_access_key='')


table = dynamodb.Table('Login')

response = table.query( KeyConditionExpression=Key('username').eq(username) & Key('password').eq(password) )
items = response['Items']

if items:
    table = dynamodb.Table('Movies')
    items=table.scan()['Items']        
    print("<table border='2'>")
    print("<tr>")
    print("<th>Movie Id</th>")
    print("<th>Movie Name</th>")
    print("</tr>")
    for item in items:
        print("<tr>")
        print("<td>{0}</td>".format(items[0]))
        print("<td>{0}</td>".format(items[1]))
        print("</tr>")
    print("</table>")
#print(json.dumps(item, indent=4, cls=DecimalEncoder))
else:
    pymsgbox.alert('Incorrect username or password', 'Error!',button='OK')

