
---
# Diamond Price Prediction

## Overview

This project is designed to predict diamond prices using a Machine Learning model. It includes data ingestion, transformation, model training, and prediction. The project is implemented using Python and Flask .

## Dataset Link
[Diamond Price Dataset](https://www.kaggle.com/competitions/playground-series-s3e8/data)

### Features
The dataset consists of 10 independent variables (including `id`):
- **id**: Unique identifier for each diamond.
- **carat**: Carat (ct.) is the unit of weight measurement used exclusively for gemstones and diamonds.
- **cut**: Quality of the diamond cut.
- **color**: Color of the diamond.
- **clarity**: A measure of the purity and rarity of the stone, graded by visibility under 10-power magnification.
- **depth**: Height (in millimeters) measured from the culet (bottom tip) to the table (flat top surface).
- **table**: The facet of the diamond visible when viewed face up.
- **x**: Diamond X dimension.
- **y**: Diamond Y dimension.
- **z**: Diamond Z dimension.

### Target Variable
- **price**: Price of the given diamond.

### Project Structure
```bash
DiamondPricePrediction/
├── .dvc
├── .github/workflows/
│           └── main.yaml
├── src/
│   ├── DiamondPricePrediction/
│   │   ├── components/
│   │   │   ├── data_ingestion.py
│   │   │   ├── data_transformation.py
│   │   │   ├── model_evaluation.py
│   │   │   └── model_training.py
│   │   ├── pipelines/
│   │   │     ├── prediction_pipeline.py
│   │   │     └── training_pipeline.py
│   │   ├── utils.py/
│   │   │    └── utils.py
│   │   ├── exception.py
│   │   ├── logger.py
├── templates/
│   ├── index.html
│   ├── predict.html
│   └── result.html
├── app.py
├── Dockerfile
├── dvc.yaml
├── init_setup.sh
├── README.md
├── requirements.txt
├── setup.py
└── template.py
```

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/kunalshelke90/DiamondPricePrediction.git
    cd DiamondPricePrediction
    ```

2. **Create a virtual environment and install dependencies(if you have linux base terminal)**:
    ```bash
    bash init_setup.sh
    ```
    # Else

    **Create a virtual environment and install dependencies**:
    ```bash 
    conda create env -p Diamond_Price python=3.8 -y
    ```
    ```bash
    conda activate Diamond_Price
    ```
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
   Create a `.env` file in the project root and add the following variables:
    ```plaintext
    DAGSHUB_REPO_OWNER="owner_name"
    DAGSHUB_REPO_NAME="Repo_name"
    DAGSHUB_MLFLOW="True"
    MLFLOW_REGISTRY_URI="https://dagshub.com/repo_owner/repo_name.mlflow"

    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    ```

## Usage

1. **Start the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the application**:
   Open your web browser and navigate to [http://localhost:8080](http://localhost:8080) or [http://127.0.0.1:8080](http://127.0.0.1:8080) to interact with the application.

## Using Docker

1. **Build the Docker image**:
    ```bash
    docker build -t Diamond .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 5000:5000 Diamond
    ```

## Customization

1. **Data Ingestion**:
   Customize `data_ingestion.py` in the `src/DiamondPricePrediction/components` folder to suit your data source and schema. Modify the connection settings for your Cassandra database and adjust the data loading logic in `src/mlproject/utils.py`.

2. **Data Transformation**:
   Modify `data_transformation.py` in the `src/DiamondPricePrediction/components` folder to apply different scaling methods, feature engineering techniques, or transformations according to your dataset's needs.

3. **Model Training**:
   Customize `model_training.py` in the `src/DiamondPricePrediction/components` folder to experiment with different models, hyperparameters, and evaluation metrics. You can also integrate other ML libraries like TensorFlow or PyTorch.

4. **Web Interface**:
   Modify the HTML templates in the `templates/` folder to match your preferred UI design. You can add or remove input fields, change styles, and customize the prediction output format.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
---
