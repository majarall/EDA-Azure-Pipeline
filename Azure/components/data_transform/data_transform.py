
import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
import logging
import mlflow


def main():
    """Main function of the script."""

    # input and output arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, help="path to input data")
    parser.add_argument("--test_train_ratio", type=float, required=False, default=0.25)
    parser.add_argument("--train_data", type=str, help="path to train data")
    parser.add_argument("--test_data", type=str, help="path to test data")
    args = parser.parse_args()

    # Start Logging
    mlflow.start_run()

    print("input data:", args.data)
    delimeter = ";"
    df = pd.read_csv(args.data, sep=delimeter)
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    # drop feature with missing values
    df.drop("feature_3", axis=1, inplace=True)
    # select best features + target
    cols = ["y","feature_1","feature_2", "feature_4","feature_9"]
    df = df[cols]

    mlflow.log_metric("num_samples", df.shape[0])
    mlflow.log_metric("num_features", df.shape[1] - 1)

    df_train, df_test = train_test_split(df,test_size=args.test_train_ratio,)

    # output paths are mounted as folder, therefore, we are adding a filename to the path
    df_train.to_csv(os.path.join(args.train_data, "data.csv"), index=False)

    df_test.to_csv(os.path.join(args.test_data, "data.csv"), index=False)

    # Stop Logging
    mlflow.end_run()


if __name__ == "__main__":
    main()
