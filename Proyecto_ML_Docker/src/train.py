import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

def main():
    parser = argparse.ArgumentParser(description="Train a simple regression model")
    parser.add_argument("--data", type=str, required=True, help="Path to CSV dataset")
    parser.add_argument("--output", type=str, required=True, help="Path to save trained model (e.g., model.pkl)")
    args = parser.parse_args()

    # Load dataset
    df = pd.read_csv(args.data)
    # Assume last column is target, rest are features
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    # Save model
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    joblib.dump(model, args.output)
    print(f"Model trained and saved to {args.output}")

if __name__ == "__main__":
    main()
