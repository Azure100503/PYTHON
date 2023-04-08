import re


def regex_remove():
    html_tag = re.compile(r'<.*?>')
    number = re.compile(r'\d+')

    with open('test.csv', 'r') as input_file:
        data = input_file.read()
        data = re.sub(html_tag, '', data)
        data = re.sub(number, '', data)

    with open('cleaned.csv', "w") as output_file:
        output_file.write(data)


regex_remove()
