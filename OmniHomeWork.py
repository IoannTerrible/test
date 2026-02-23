# So Homework.... work again. Okay okay. Let's try to compelte all course homework in one file.
# Coding Assigment 1 Classe
# Well in mine Superion C# language we have Classes and Structs. Classes are relative and struct are value-types. Class lays in Heap
# Structs lays in stack. You can't inherit struct.  Task required me to create random classs with methods and Properties (I will use C# naming, but I understand difference)

from datetime import date
#In C# we have it build-in

class Homework():
    def __init__(self, name: str, author: str):
        self.name = name
        self.date_of_subbmission = date.today()   # In C# We have DateTime and DateTimeOffset. diference in
        self.author = author
        self.grade = 0
    
    def assign_author(self, author: str):
        if(author is not None): #In C# we write Null instead of None
            self.author = author 
        #In C# we have String.IsNullOrEmpty because null and "" is different
    
    def grade_homeWork(self, grade: int): 
        if(grade < 0):
            raise ValueError("Error")
            #throw new Exeption("Smth wrong") # C# version, In C# we even can just throw. it will provide error up to call stack
        self.grade = grade

    # In C# we have ToString method. and it has protected modifyier. 
    # We do not create new method in c# we override method from class "Object" that parent to all classes in .Net
    def __str__(self):
        return(f"Hiii, my name is {self.name}, I am {self.grade} points old")
    

hw = Homework("Coding Assigments 1", "TheRR")
hw.grade_homeWork(90)
print(hw)

# Seems okay. Now about Inheritance

# Fun and scary fact. Python allows multiple inheritance, Very scary but it's goes from left to right.
class EnglishHomeWork(Homework):
    def __init__(self, name, author):
        # In C# we can call it base.MethodName()
        super().__init__(name, author)

    def assign_author(self, author: str):
        print("For some reason no Author for english homework")
        print(f"Your author was {author}")


#Python allows import anywhere in file. 
#I think we need class about modules and namespaces like from where we can import and what we "see"
import random
import os


eng_hw = EnglishHomeWork("English Essay", "Ronald")

random_grade = random.randint(0, 100)
eng_hw.grade_homeWork(random_grade)

# I checked the syllabus, and the next topic is files. Interesting fact:
# On work, I usually do not interact with files. I have only 2 functions that work with files directly.

#Yeah. It is. I even saw people create programm to turn .rar archives to .mp3 and upload to Yt to use it as Storage
file_name = "test.extentionIsAjoke"
# In C# we can call directly. Directory... etc
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

# Good Architecture.
# With is like using in C#. If I Understand weak interpreter correctly in Python it is too try smth -> dispose
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        metadata = f"File created at: {date.today()} | Author: {eng_hw.author}\n"
        f.write(metadata)

# Read file and print content, We open with read and using unicode encoding.
# We can use as X-Mode any linux like modes like r+ and others. Check docs
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    # We can do some stuff in read mode for example
    lines = f.readlines()

print(content)
print(len(lines))
#I belive looks good.

#Next code assigment. Console Programms. Not sure what you mean by this, Since our programms already console
#I just show that I know how to read docs and change color of console in cycle so you can choose what is best.

def change_console_color():
    #Should work
    colors = [
        "\033[91m",  # Red
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
    ]
    
    random_color = random.choice(colors)
    print(random_color + "Color is chandged")


#Proper python file indeed. 
#It will run only if we run this file, 
if __name__ == "__main__":
    # Main cycle. Like in games or rendering.
    while True:
        answer = input("Change color? (Y/N): ")

        #In C# we can do that. Or use Equals.
        if answer.lower() == "y":
            change_console_color()
        else:
            print("Let's see other homeworks")
            break

#Next theme is Git and GitLab. Well You pretty sure know that I am aware of git push git commit.
#Actually I have cool Git CICD for my nugets packages. When I push to "product" branch in mine pet projects
#It will run job that compile project, run tests, compile it to nuget package, And IF version is different it pushed it
#To Nuget library. Pretty cool isn't it? I think counts as home work


#Well well well. Web Scarping. Good Old Html.Parse never betray me. My Discord Notifications bot work on it. Because I
#Because I suggest Twithc API with OAuth 2.0 to complicated for just notifications.
#As example I use Cool old. Example.com
# We may actually neded html.parser but. We can be html parsers by ourselfs. since it just long string. 

import urllib.request

url = "http://example.com"

with urllib.request.urlopen(url) as response:
    html = response.read().decode("utf-8")

title = html.split("<h1>")[1].split("</h1>")[0]
paragraphs = html.split("<p>")

paragraph_block = paragraphs[2].split("</p>")[0]
if 'href="' in paragraph_block:
    link = paragraph_block.split('href="')[1].split('"')[0]
else:
    link = None

print("Link Web Scarping inside:", link)


# Okay. I think It will do before Midtherm