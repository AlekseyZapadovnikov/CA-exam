#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
WARNING: bad code style

Generate report:

clang matrix.c && \ 
   time ( echo "size\tmul\ttrans\tcomplexity" && seq 0 20 3500 | xargs -n1 -P4 ./a.out | sed 's/\./,/g' ) && \
   time ( echo "size\tmul\ttrans\tcomplexity" && seq 0 20 3500 | xargs -n1 ./a.out | sed 's/\./,/g')
*/

int **mk_matrix(int size, int limit) {
  int **A = malloc(size * sizeof(int *));
  if (A == NULL) return NULL;
  for (int i = 0; i < size; i++) {
    A[i] = malloc(size * sizeof(int));
    if (A[i] == NULL) {
      for (i = i - 1; i >= 0; i--) free(A[i]);
      free(A);
      return NULL;
    }
    for (int j = 0; j < size; j++) {
      A[i][j] = rand() % limit ? limit != 0 : 0;
    }
  }
  return A;
}

void free_matrix(int size, int **A) {
  for (int i = 0; i < size; i++) {
    free(A[i]);
  }
  free(A);
}

int **transpose(int size, int **A) {
  int **B = mk_matrix(size, 1);
  if (B == NULL) return NULL;
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      B[j][i] = A[i][j];
    }
  }
  return B;
}

int **mul(int size, int **A, int **B) {
  int **C = mk_matrix(size, 1);
  if (C == NULL) return NULL;

  clock_t start = clock();
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      C[i][j] = 0;
      for (int k = 0; k < size; k++) {
        C[i][j] += A[i][k] * B[k][j];
      }
    }
  }
  clock_t end = clock();
  float seconds = (float)(end - start) / CLOCKS_PER_SEC;
  printf("%d\t%.4lf\t", size, seconds);
  return C;
}

int **mul_transpose(int size, int **A, int **B) {
  int **B2 = NULL, **C = NULL;

  B2 = transpose(size, B);
  if (B2 == NULL) return NULL;

  C = mk_matrix(size, 1);
  if (C == NULL) goto error1;

  clock_t start = clock();
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      C[i][j] = 0;
      for (int k = 0; k < size; k++) {
        C[i][j] += A[i][k] * B2[j][k];
      }
    }
  }
  clock_t end = clock();
  float seconds = (float)(end - start) / CLOCKS_PER_SEC;
  double s = (double)size;
  printf("%.4lf\t%.0f\n", seconds, s * s * s);

error1:
  free_matrix(size, B2);
  return C;
}

void print_matrix(int size, int **mat) {
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      printf("%d\t", mat[i][j]);
    }
    printf("\n");
  }
}

int main(int argc, char *argv[]) {
  if (argc != 2) return 128;
  int size = atoi(argv[1]);
  if (size == 0) return 128;

  int **A = mk_matrix(size, 10);
  if (A == NULL) return EXIT_FAILURE;
  int **B = mk_matrix(size, 10);
  if (B == NULL) return EXIT_FAILURE;

  // printf("size\tmul\ttrans\tcomplexity\n");
  int **C1 = mul(size, A, B);
  if (C1 == NULL) return EXIT_FAILURE;

  int **C2 = mul_transpose(size, A, B);
  if (C2 == NULL) return EXIT_FAILURE;

  free_matrix(size, A);
  free_matrix(size, B);
  free_matrix(size, C1);
  free_matrix(size, C2);

  return EXIT_SUCCESS;
}
