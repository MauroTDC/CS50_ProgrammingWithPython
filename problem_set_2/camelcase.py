def main():
    camel_to_snake(input("camelCase: "))


def camel_to_snake(variable: str) -> None:
    snake_case = ""
    for i in range(len(variable)):
        if variable[i].isupper():
            if i > 0:
                snake_case += "_" + variable[i].lower()
            else:
                snake_case += variable[i].lower()
        else:
            snake_case += variable[i]
    print(snake_case)
       
        
if __name__ == "__main__":
    main()