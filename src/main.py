import knn, pca, image_operations, load_image_vectors

tests_count = 0
tests_success = 0


def set_success_rate(prediction, test_image) -> None:
    global tests_count, tests_success
    if prediction == test_image.label:
        tests_success += 1
    tests_count += 1
    return None


def get_success_rate ():
    global tests_count, tests_success
    success = float(tests_success)/float(tests_count)
    return round(success, 4)


if __name__ == '__main__':
    k = 20  # number of nearest neighbors to check
    training_gz = load_image_vectors.load_gz('../data/mnist_train.csv.gz')
    training_list = load_image_vectors.get_image_object_list(training_gz)
    print("Successfully loaded training list")
    test_gz = load_image_vectors.load_gz('../data/mnist_test.csv.gz')
    test_list = load_image_vectors.get_image_object_list(test_gz)
    print("Successfully loaded test list")

    # training_csv = load_image_vectors.load_csv('../data/mnist_train.csv') # Alternative to load_gz
    for i in range (10):
        sorted_distances = knn.get_sorted_distances(test_list[i], training_list)
        # print("Successfully calculated distance of one test image to all training images")
        predicted_digit = knn.knn_distance_prediction(sorted_distances,k)
        set_success_rate(predicted_digit, test_list[i])
    print("Success rate: " + str(get_success_rate()))