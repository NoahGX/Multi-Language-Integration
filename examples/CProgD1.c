#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int *arrayPtr = NULL;
    int arraySize = argc - 1; // First argument is program name
    int threshold = 170;

    // Verify number of arguments
    if (argc < 2) {
        printf("Error: No numbers provided in command line.\n");
        exit(1);
    }

    // Dynamically allocate memory
    arrayPtr = (int*)malloc(arraySize * sizeof(int));
    if (arrayPtr == NULL) {
        printf("Error: Unable to allocate memory.\n");
        exit(1);
    }

    // Convert arguments to integers and store in array
    for (int i = 0; i < arraySize; i++) {
        arrayPtr[i] = atoi(argv[i + 1]);
    }
    
    // Add 1 to each element and print
    for (int i = 0; i < arraySize; i++) {
        printf("%d ", arrayPtr[i] + 1);
    }
    printf("\n");

    // Free dynamically allocated memory
    free(arrayPtr);
    arrayPtr = NULL;
    return 0;
}
