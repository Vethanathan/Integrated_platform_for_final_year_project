import os
import openai
def answer(argument):
    openai.api_key = ""
    # argument = "what is your purpose?"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=argument,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return str(response.choices[0].text)

# print(answer('#include <stdio.h> #include <stdlib.h> int main() { char sentence[1000]; // creating file pointer to work with files FILE *fptr; // opening file in writing mode fptr = fopen("program.txt", "w"); // exiting program if (fptr == NULL) { printf("Error!"); exit(1); } printf("Enter a sentence:\n"); fgets(sentence, sizeof(sentence), stdin); fprintf(fptr, "%s", sentence); fclose(fptr); return 0; }'))
