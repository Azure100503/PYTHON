import re

def label_data():
    with open("/Users/nguyenthihuyensam/PycharmProjects/pythonProject/output.txt", "a") as output_file:
        while True:
            sentence = input("Enter a sentence: ")
            keywords = []
            labels = []
            entities = []

            while True:
                keyword = input("Enter a keyword : ")
                if keyword == '0':
                    break
                label = input("Enter the label : ")
                keywords.append(keyword)
                labels.append(label)

            for i, keyword in enumerate(keywords):
                for match in re.finditer(re.escape(keyword), sentence):
                    start = match.start()
                    end = match.end()
                    label = labels[i]
                    entities.append((start, end, label))

            output = {'entities': entities}
            print(sentence, output)
            output_file.write(f"{sentence}: {'/Users/nguyenthihuyensam/PycharmProjects/pythonProject/output.txt'}\n")


label_data()