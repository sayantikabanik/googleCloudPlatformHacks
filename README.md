# googleCloudPlatformHacks
## Few simply awesome tricks to start with GCP for complete beginners 
GCP documentation for a beginner like me was little to complicated. As i keep learning
i will be commiting the tips and tricks.

## Getting started with Google-Cloud-storage
How to transfer your files from the local host to the GCP bucket?
I am using python(2.7) API with Ubuntu/Debian for developemnt purpose
After the login and payment credentials are initiated, we can start up with the developemt process.

Download the sdk:
``` fancy
$ curl https://sdk.cloud.google.com | bash
```
``` fancy
$pyhton 
>>>gcloud -h | less 

```
(no error, then it worked)
``` fancy
$ gcloud auth login 
```
(Enter password and login id for your account)

After the above steps are successfully completed, run the python file.
``` fancy
$ python transferToGcpBucket.py
```
