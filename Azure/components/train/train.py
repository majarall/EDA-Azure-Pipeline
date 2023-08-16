import argparse
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import os
import pandas as pd
import mlflow


def select_first_file(path):
    """Selects first file in folder, use under assumption there is only one file in folder
    Args:
        path (str): path to directory or file to choose
    Returns:
        str: full path of selected file
    """
    files = os.listdir(path)
    return os.path.join(path, files[0])


# Start Logging
mlflow.start_run()

# enable autologging
mlflow.sklearn.autolog()

os.makedirs("./outputs", exist_ok=True)


def main():
    """Main function of the script."""

    # input and output arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_data", type=str, help="path to train data")
    parser.add_argument("--test_data", type=str, help="path to test data")
    parser.add_argument("--n_estimators", required=False, default=100, type=int)
    parser.add_argument("--max_leaf_nodes", required=False, default=50, type=int)
    parser.add_argument("--registered_model_name", type=str, help="model name")
    parser.add_argument("--model", type=str, help="path to model file")
    args = parser.parse_args()

    # paths are mounted as folder, therefore, we are selecting the file from folder
    train_df = pd.read_csv(select_first_file(args.train_data))

    # Extracting the label column
    y_train = train_df.pop("y")

    # convert the dframe values to array
    X_train = train_df.values

    # paths are mounted as folder, therefore, we are selecting the file from folder
    test_df = pd.read_csv(select_first_file(args.test_data))

    # Extracting the label column
    y_test = test_df.pop("y")

    # convert the dframe values to array
    X_test = test_df.values

    print(f"Training with data of shape {X_train.shape}")

    model = RandomForestRegressor(
        n_estimators=args.n_estimators, max_leaf_nodes=int(args.max_leaf_nodes)
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(mean_absolute_error(y_test, y_pred))

    # Registering the model to the workspace
    print("Registering the model via MLFlow")
    mlflow.sklearn.log_model(
        sk_model=model,
        registered_model_name=args.registered_model_name,
        artifact_path=args.registered_model_name,
    )

    # Saving the model to a file
    mlflow.sklearn.save_model(
        sk_model=model,
        path=os.path.join(args.model, "trained_model_3"),
    )

    # Stop Logging
    mlflow.end_run()


if __name__ == "__main__":
    main()
