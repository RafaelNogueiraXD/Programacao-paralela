char knn(Point* all_points, char* all_labels, int total_points, int k, Point to_evaluate){
    float *dev_all_distances;
    char *dev_label_distances;
    Point *dev_all_points;
    char *dev_all_labels;
    cudaError_t err;

    printf("antes do malloc e tamanho total: %d\n", total_points);

    err = cudaMalloc((void**)&dev_all_points, total_points * sizeof(Point));
    if (err != cudaSuccess) {
        printf("Erro ao alocar dev_all_points: %s\n", cudaGetErrorString(err));
        return -1;
    }
    printf("aloquei 1\n");

    err = cudaMalloc((void**)&dev_all_labels, total_points * sizeof(char));
    if (err != cudaSuccess) {
        printf("Erro ao alocar dev_all_labels: %s\n", cudaGetErrorString(err));
        return -1;
    }
    printf("aloquei 2\n");

    err = cudaMalloc((void**)&dev_all_distances, total_points * sizeof(float));
    if (err != cudaSuccess) {
        printf("Erro ao alocar dev_all_distances: %s\n", cudaGetErrorString(err));
        return -1;
    }
    printf("aloquei 3\n");

    err = cudaMalloc((void**)&dev_label_distances, total_points * sizeof(char));
    if (err != cudaSuccess) {
        printf("Erro ao alocar dev_label_distances: %s\n", cudaGetErrorString(err));
        return -1;
    }
    printf("aloquei 4\n");

    printf("antes do memcpy\n");

    err = cudaMemcpy(dev_all_points, all_points, total_points * sizeof(Point), cudaMemcpyHostToDevice);
    if (err != cudaSuccess) {
        printf("Erro ao copiar dev_all_points: %s\n", cudaGetErrorString(err));
        return -1;
    }

    err = cudaMemcpy(dev_all_labels, all_labels, total_points * sizeof(char), cudaMemcpyHostToDevice);
    if (err != cudaSuccess) {
        printf("Erro ao copiar dev_all_labels: %s\n", cudaGetErrorString(err));
        return -1;
    }

    printf("antes do dim3\n");

    dim3 threads(128);
    dim3 blocks((total_points + (threads.x - 1)) / threads.x);

    printf("antes do kernel\n");
    calcular_distancia<<<blocks, threads>>>(dev_all_points, dev_all_labels, dev_all_distances, dev_label_distances, total_points, k, to_evaluate);

    err = cudaGetLastError();
    if (err != cudaSuccess) {
        printf("Erro no kernel calcular_distancia: %s\n", cudaGetErrorString(err));
        return -1;
    }

    printf("terminei as distancias\n");

    float* dev_sorted_distances;
    char* dev_sorted_labels;

    err = cudaMalloc(&dev_sorted_distances, total_points * sizeof(float));
    if (err != cudaSuccess) {
        printf("Erro ao alocar dev_sorted_distances: %s\n", cudaGetErrorString(err));
        return -1;
    }

    err = cudaMalloc(&dev_sorted_labels, total_points * sizeof(char));
    if (err != cudaSuccess) {
        printf("Erro ao alocar dev_sorted_labels: %s\n", cudaGetErrorString(err));
        return -1;
    }

    ordenar_distancias(dev_all_distances, dev_sorted_distances, dev_label_distances, dev_sorted_labels, total_points);

    char* k_menores_labels = (char*)malloc(k * sizeof(char));
    cudaMemcpy(k_menores_labels, dev_sorted_labels, k * sizeof(char), cudaMemcpyDeviceToHost);

    char resultado = calcular_mais_frequente(k_menores_labels, k);
    return resultado;
}
