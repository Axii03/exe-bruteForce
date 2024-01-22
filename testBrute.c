#include <stdio.h>
#include <string.h>

#define MAX_CODE_LENGTH 50
#define CORRECT_CODE "123456"

int main() {
    char enteredCode[MAX_CODE_LENGTH];

    printf("Enter the secret code: ");
    fgets(enteredCode, sizeof(enteredCode), stdin);

    enteredCode[strcspn(enteredCode, "\n")] = '\0';

    if (strcmp(enteredCode, CORRECT_CODE) == 0) {
        printf("Access granted! Flag: {AxiiST3$tf1@g}\n");
    } else {
        printf("Access denied\n");
    }

    return 0;
}

