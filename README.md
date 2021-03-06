# Keras Sentiment

A basic sentiment classifier in Keras.

## Setup

```
$ pip3 install --user -r requirements.txt
$ ln $PATH_TO_REVIEWS_SQLITE reviews.sqlite
$ ln $PATH_TO_EMBEDDINGS embeddings.txt
```

To setup the sentiment model server, follow the [tensorflow serving install instructions](https://www.tensorflow.org/serving/setup#installing_modelserver).

## Model Training

Run the jupyter notebook:

```
$ jupyter notebook
```

## Tensorflow Serving

```
$ docker run -it --runtime=nvidia -p 8501:8501   --mount type=bind,source=$(pwd)/out/sentiment,target=/models/sentiment   -e MODEL_NAME=sentiment -t tensorflow/serving:latest 
```

### GPU

```
$ docker run -it --runtime=nvidia -p 8502:8501   --mount type=bind,source=$(pwd)/out/sentiment,target=/models/sentiment   -e MODEL_NAME=sentiment -e CUDA_VISIBLE_DEVICES=0 -t tensorflow/serving:latest-gpu 
```

### Example Payload

```
$ curl --request POST \
  --url http://localhost:8501/v1/models/sentiment/versions/1:predict \
  --header 'content-type: application/json' \
  --data '{
	"instances": [[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
        189, 351,  31,  31,  97, 498,   6, 347, 110 ], [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0, 131,  27,   7,  13,  48,   1]]
}'
```

## Cloud Deployment

### Export

```bash
$ ./export_model.py
```

### Upload to GCS

Set version first!

```bash
$ export VERSION=4
```

```bash
$ gsutil rsync -r out/sentiment/1/ gs://axelbrooke-models/keras-sentiment/$VERSION
```

### Create New Version

```bash
$ gcloud ml-engine versions create "v$VERSION" --model "keras_sentiment" --origin gs://axelbrooke-models/keras-sentiment/$VERSION/ --runtime-version 1.10
```

## Cloud Prediction

```bash
$ time gcloud ml-engine predict --model=keras_sentiment --json-instances=instances_100.json
```

Note: we see ~80 predictions per second per single core machine (with 100-item batches).

