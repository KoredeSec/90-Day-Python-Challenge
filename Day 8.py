#a script that reads a text file and counts how many lines and words are in the file.

file_path ="C:/Users/yusuf/OneDrive/Desktop/Tory.txt"

def count_lines_and_words(file_path):
        with open(file_path, "r") as file:
         line_count = 0
         word_count = 0
         content = file.read()
         print(content)
        for line in content.splitlines():
            line_count += 1
            word_count += len(line.split())
            return line_count, word_count
line_count, word_count = count_lines_and_words(file_path)
              
            

print(f"Lines : {line_count}")
print(f"Words : {word_count}")
           
