# Deploy-to-Cloud-Run

## Installation

We have to install everything in requirements.txt with pip;
```bash
  $ pip install -r requirements.txt
```

## Run Flask
Run the code below to ensure that the server is running locally and make sure you get a response
```bash
  $ python3 main.py
```

## Docker 
We use docker, enter your `gcp project ID` and the `name of the image` to create.
```bash
docker build -t gcr.io/[PROJECT-ID]/[IMAGE-NAME]:[TAG] .
```

```bash
docker push gcr.io/[PROJECT-ID]/[IMAGE-NAME]:[TAG]
```

## GCP
Open a gcp account, then go to Container Registry and you will see the docker image that has been created. After that, click `deploy to Cloud Run` with port `8000`.

## Endpoint
https://serenepath-v1-rdvq4vqihq-et.a.run.app/predict

## Books
### Recommendation Content Based
- Method : `POST`
- Key  : `text`
- Value  : as `string`

**Response**
```bash
{
  "Text": "saya sehat",
  "Label": "Tidak depresi",
  "Probability": 0.4455435574054718
}
```
