### Daimond Price Prediction

# Overview

This project is designed to predict predict Diamond price using a machine learning model. It includes data ingestion, transformation, model training,and prediction. The project is implemented using Python and Flask.


# DatasetLink
```
https://www.kaggle.com/competitions/playground-series-s3e8/data

```
There are 10 independent variables (including `id`):
* `id` : unique identifier of each diamond
* carat : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
* cut: Quality of Diamond Cut
* color: Color of Diamond
* clarity: Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these
characteristics under 10-power magnification.
* 'depth : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top
surface)
* table: A diamond's table is the facet which can be seen when the stone is viewed face up.
* x: Diamond X dimension
* y: Diamond Y dimension
* x: Diamond Z dimension
Target variable:
* `price`: Price of the given Diamond.

# Installation

1. Clone the repository:
```
git clone https://github.com/kunalshelke90/DiamondPricePrediction.git
```
```
cd DiamondPricePrediction
```
2. Create a virtual environment and install dependencies:

```
bash init_setup.sh
```
3. Set up ".env" environment variables:

```
DAGSHUB_REPO_OWNER="owner_name"
DAGSHUB_REPO_NAME="Repo_name"
DAGSHUB_MLFLOW="True"
MLFLOW_REGISTRY_URI="https://dagshub.com/repo_owner/repo_name.mlflow"

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```
## Usage

1. Start the Flask application:

```
python app.py
```
2. Access the application:

Open your web browser and go to http://localhost:8080 to interact with the application. or http://127.0.0.1:8080

## using Docker

1. Build the Docker image:


```
docker build -t Gemstone .
```


```
docker run -p 5000:5000 Gemstone
```


## Customization

1. Data Ingestion:
Customize data_ingestion.py in the src/DiamondPricePrediction/components folder to suit your data source and schema. You can modify the connection settings for your Cassandra database and adjust the data loading logic in src/mlproject/utils.py .

2. Data Transformation:
Modify data_transformation.py in the src/DiamondPricePrediction/components folder to apply different scaling methods, feature engineering techniques, or transformations according to your dataset's needs.

3. Model Training:
Customize model_training.py in the src/DiamondPricePrediction/components folder to experiment with different models, hyperparameters, and evaluation metrics. You can also integrate other ML libraries like TensorFlow or PyTorch.

4. Web Interface:
Modify the HTML templates in the templates/ folder to match your preferred UI design. You can add or remove input fields, change styles, and customize the prediction output format.


## License

This project is licensed under the MIT License. See the LICENSE file for more details.

