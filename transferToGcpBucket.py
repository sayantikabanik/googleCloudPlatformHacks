import os

os.system('gsutil cp filename.extention gs://botofficer')
#single file with extentions ranging from (.txt,jpg,.csv)

os.system('gsutil -m cp -r foldername gs://botofficer')
#folder upload
