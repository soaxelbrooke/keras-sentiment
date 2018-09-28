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

## Serving

```
$ tensorflow_model_server --model_base_path=$(pwd)/out/sentiment --model_name=sentiment --rest_api_port=9000 
```

### Example Payload

```
$ curl --request POST \
  --url http://localhost:9000/v1/models/sentiment/versions/1:predict \
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
