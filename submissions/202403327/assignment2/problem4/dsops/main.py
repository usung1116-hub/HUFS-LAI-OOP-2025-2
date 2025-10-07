from dsops import train_test_split, label_distribution
if __name__ == "__main__":
    print("--- train_test_split Demo ---")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    train, test = train_test_split(data, test_ratio=0.3, seed=42)
    print(f"Original data: {data}")
    print(f"Train set: {train}")
    print(f"Test set:  {test}")

    print("\n--- label_distribution Demo ---")
    labels = ["cat", "dog", "cat", "bird", "dog", "cat"]
    dist = label_distribution(labels)
    print(f"Labels: {labels}")
    print(f"Distribution: {dist}")