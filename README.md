# kfood-server

Korean food image recognition API server implemented using Django and TensorFlow

API Access:

http://127.0.0.1:8000/api/classify

form-data:
```
{
  photo: bibimbab_photo.jpg
}
```

returns:
```
{
  "class": "bibimbab",
  "success": true
}
```
