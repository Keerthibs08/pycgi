#!C:\Users\Keerthi\AppData\Local\Programs\Python\Python38-32\python.exe
import boto3
import cgi,cgitb
import pymsgbox

print("Content-type: text/html\r\n\r\n")

form=cgi.FieldStorage()

username=form.getvalue("username")
password=form.getvalue("password")

dynamodb = boto3.resource('dynamodb',region_name='us-east-2',
    aws_access_key_id='',
    aws_secret_access_key='')


table = dynamodb.Table('Login')

response = table.put_item(
  Item={
       'username': username,
       'password': password,
   }
)

message = pymsgbox.alert('Registered succesfully','ok') 
