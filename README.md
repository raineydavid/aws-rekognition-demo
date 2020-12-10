# Amazon Rekognition Demo Scripts
A collection of demos using Amazon Rekognition

## capture.py
Capture a photo from local camera or file, run Amazon Rekognition to detected objects in the photo, then generate an Amazon Polly voice that describes the photo.
In case there are humans in the photo, the code will run Amazon Rekognition again to detect faces.

Usage:
```
capture.py [image_path]

* Use with no arguments to take a photo with the camera, or one argument to use a saved image
```

## search_face.py
Capture a photo from local camera or file, run Amazon Rekognition to detect faces and them try to match detected faces to a specific collectionId.

Usage:
```
search_face.py [image_path]

* Use with no arguments to take a photo with the camera, or one argument to use a saved image
```

## comapare.py
Compare two images using Rekognition

Usage:
```
compare.py image_1_path image_2_path
```
## match.py
Match an image to a collection

Usage:
```
match.py image_path collection_name
```
