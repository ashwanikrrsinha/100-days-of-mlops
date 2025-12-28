import random 
import argparse

def train_model(n_estimators:int, max_depth:int) -> float:
    """
    Simulates training a Random forest model

    Args:
        n_estimators (int): Number of trees in the forest.
        max_depth (int): Maximum depth of the tree.
    
    Returns:
        float: Simulated accuracy of the trained model.
    """
    
    # Simulate some training logic
    print(f"Training model with {n_estimators} trees and max depth of {max_depth}...")

    # simulate an accuracy score based on parameters
    accuracy = 0.5 + (0.1 * random.random())
    
    return accuracy

if __name__ == "__main__":
    #this block only runs if you execute the script directly
    # e.g. python model.py

    # Initialize the parser
    parser = argparse.ArgumentParser(description="Train a dummy model.")
    
    # Add arguments
    parser.add_argument("--n_estimators", type=int, default=100, help="Number of trees")
    parser.add_argument("--max_depth", type=int, default=5, help="Max depth of trees")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Use the arguments
    result = train_model(n_estimators=args.n_estimators, max_depth=args.max_depth)
    print(f"Model Training Complete. Accuracy: {result}")
