def custom_write(file_name, strings):
    strings_positions = {}
    
    with open(file_name, 'w', encoding='utf-8') as f:
        for index, string in enumerate(strings, start=1):
            position = f.tell() 
            
            f.write(string + '\n') 
         
            strings_positions[(index, position)] = string

    return strings_positions

# Пример использования:
file_name = 'output.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.']
result = custom_write(file_name, strings)
print(result)