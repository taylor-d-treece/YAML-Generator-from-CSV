import os
import csv

# Enter Desired Working Directory Below
if os.getcwd() != '':
    os.chdir('')

# Enter filename CSV to generate YAML from
with open('Your_File_Here.csv', mode='r') as file:
    csvFile = csv.reader(file)
    YAML_item_list = list(csvFile)

# Enter Desired Saved Filename on Line Below
with open('Generated_YAML.yaml', 'a+') as output:
    output.write('# Generated YAML FILE\n')
    output.write('---\n')
    output.write('item:\n')
    for i in range(len(YAML_item_list)):
        # List indexes such as "YAML_item_list[i][0]" correspond to the data within the CSV columns
        # Index 0 == Data in Column 1, Index 1 == Data in Column 2, etc
        output.write('- field1: "{}"\n'.format(YAML_item_list[i][0]))
        output.write('  field2: "{}"\n'.format(YAML_item_list[i][1]))
        output.write('  field3: "{}"\n'.format(YAML_item_list[i][2]))
        output.write('  field4:\n')
        # List Items Below - Can be modified to fit data and use optional "If" statments if data may be missing
        # Please reach out with any questions or if help is needed!
        output.write('  - "{}"\n'.format(YAML_item_list[i][2]))
        if question_list[i][3] != '':
            output.write('  - "{}"\n'.format(YAML_item_list[i][3]))
        if question_list[i][3] != '':
            output.write('  - "{}"\n'.format(YAML_item_list[i][4]))
    output.close()
