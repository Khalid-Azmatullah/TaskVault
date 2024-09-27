import pyfiglet
import subprocess
print(pyfiglet.figlet_format('TASK VAULT'))
print('\n Type \'help\' to get the list of available commands.')
while True:
  command = input('\n$ ')
  
  codeList=['c', 'q', 'w3c', 'help', 'exit']
  
  if command == codeList[0]: #chrome
    subprocess.Popen([r'C:/Program Files/Google/Chrome/Application/chrome.exe', '--guc.est'])
  elif command.split(' ')[0] == codeList[1]: #web search
    user_input = command.lstrip('.w ')
    subprocess.Popen([r'C:/Program Files/Google/Chrome/Application/chrome.exe', '--guest', f'https://www.google.com/search?q={user_input}'])
  elif command == codeList[2]: #c++ syntax
    subprocess.Popen([r'C:/Program Files/Google/Chrome/Application/chrome.exe', '--guest', 'https://www.w3schools.com/cpp/default.asp'])
  elif command == codeList[3]: #help
    command_list = '\nCOMMAND LIST: \n1. c - Opens Chrome in Guest mode. \n2. q - Searches your query in chrome. \n3. w3c - Opens the C++ Syntax page. \n4. help - Provides list of commands available in TaskVault. \n5. exit - Exits the program.'
    print(command_list)
  elif command == codeList[4]: #exit
    quit()