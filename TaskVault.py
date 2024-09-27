# TASK VAULT

 # Import dependencies

 # personal extension
 # from crave import *

# Important extensions
import time
import random
import sys
import subprocess
import platform
import datetime
import os
from pynput.keyboard import Key, Controller
# for keyboard 'tab'
keyboard = Controller()

 # Rich [For color and formatting]
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.spinner import Spinner
# from rich.table import Table
from rich.progress import Progress
# from rich.syntax import Syntax

 # Colorama [For input() color]
from colorama import Fore, Style

# main code
console = Console()

# title
console.print(Panel(
  " Home [magenta]|[/magenta] Notes [magenta]|[/magenta] Website [magenta]|[/magenta] Projects [magenta]|[/magenta] GitHub [magenta]|[/magenta] Youtube", title="Task Vault", title_align="center", border_style="magenta"))
#console.print("Content")
#console.print(Panel("Footer", border_style="blue"))


while True:
  # rep:
  print("" + Fore.RESET)
  input_command = input(Style.BRIGHT + "$ " + Fore.GREEN).split()

 
  count = len(input_command)
  if count >= 2:
    call = input_command[1]
    #secondary_call = input_command[2]
    #tertiary_call = input_command[3]
    ### ip-code: '-launch', '?open', '-note', '-web', '-exit'.

    ip_code = input_command[0]

    ip_list = ['launch', 'open', 'note', 'web', 'exit']

    if ip_code in ip_list:
      if ip_code == ip_list[0]:
        #? launch ==> "-*", "-ch", "-marks", "-np", "-spo", "-gpt", "-yt", "-git", "-. code", ""
        if call == "*":          
          
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          url = "https://github.com/Khalid-Azmatullah/"
          profile_directory = "Profile 2"
          subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
          
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          url = "https://www.youtube.com/"
          profile_directory = "Profile 2"
          subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
          
          
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          url = "https://open.spotify.com/"
          profile_directory = "Profile 1"
          subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
          
          
          time.sleep(4)
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          url = "https://chatgpt.com/"
          profile_directory = "Profile 2"
          subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
          
          time.sleep(8)

          # Simulate pressing the Tab key
          for _ in range(2):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
          time.sleep(1)
          keyboard.press(Key.enter)
          keyboard.release(Key.enter)
          
          time.sleep(2)
          for _ in range(8):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab) 
            
          time.sleep(6)
         
          
             
          vs_code_path = r"C:/Users/Azy/AppData/Local/Programs/Microsoft VS Code/Code.exe"  # Adjust if necessary
          # Create the command
          command = [vs_code_path]
          path = "C:/Users/Azy/Desktop/"
          if path:
            command.append(path)
            # Open VS Code and redirect stderr to DEVNULL
          with open(os.devnull, 'w') as devnull:
            subprocess.Popen(command, stderr=devnull) 
            
 
            
            
        elif call == "gpt":
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          url = "https://chatgpt.com/"
          profile_directory = "Profile 2"
          subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
          
          time.sleep(6)

          # Simulate pressing the Tab key
          for _ in range(2):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
          time.sleep(1)
          keyboard.press(Key.enter)
          keyboard.release(Key.enter)
          
          time.sleep(2)
          for _ in range(8):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        elif call == "ch":
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          # Open Chrome
          subprocess.Popen([chrome_path])
          print("")
        elif call == "marks":
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          url = "https://web.getmarks.app/"
          profile_directory = "Profile 2"
          subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
          print("")
        elif call == "np":
          program_path = r"C:\Windows\notepad.exe"
          # Open the program
          subprocess.Popen([program_path])   
          print("")
        elif call == "spo":
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          url = "https://open.spotify.com/"
          profile_directory = "Profile 1"
          subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
        elif call == "yt":
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          url = "https://www.youtube.com/"
          profile_directory = "Profile 2"
          subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
          print("")
        elif call == "git":
          chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
          url = "https://github.com/Khalid-Azmatullah/"
          profile_directory = "Profile 2"
          subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
          print("")
        elif call == ".":
          if input_command[2] == "code":    
            vs_code_path = r"C:/Users/Azy/AppData/Local/Programs/Microsoft VS Code/Code.exe"  # Adjust if necessary
            # Create the command
            command = [vs_code_path]
            path = "C:/Users/Azy/Desktop/"
            if path:
              command.append(path)
             # Open VS Code and redirect stderr to DEVNULL
            with open(os.devnull, 'w') as devnull:
              subprocess.Popen(command, stderr=devnull)
          else:
            print(Fore.RED + "ERROR: invalid launch. Try Again")
          
          print("")
        else:
          print(Fore.RED + "ERROR: invalid launch '" + Fore.GREEN + str(call)  + Fore.RED +  "'. Try Again")  
      elif ip_code == ip_list[1]:
        print("open")
      elif ip_code == ip_list[2]:
        
        user_input = ""
        count = len(input_command)
        count = count - 1
        word_count = 0
        while word_count != count:
          word_count += 1
          user_input = user_input + str(input_command[word_count]) + " "
        user_input = user_input + "\n"
        
        today = datetime.date.today()
        date = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")
        file_name = str(date) + str(month) + str(year) + ".txt"
        file_name = "Self-Notes/" + file_name
        with open(file_name, 'a') as file:
          
          file.write(user_input) 
          file.close()
      elif ip_code == ip_list[3]:
        
        user_input = ""
        count = len(input_command)
        count = count - 1
        word_count = 0
        while word_count != count:
          word_count += 1
          user_input = user_input + str(input_command[word_count]) + " "    
        chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
        url = f'https://www.google.com/search?q={user_input}'
        profile_directory = "Profile 2"
        subprocess.Popen([chrome_path, "--profile-directory=" + profile_directory, url])
      elif ip_code == ip_list[4]:
        sys.exit()
      else:
        print(Fore.RED + "ERROR: Unexpected " + Fore.GREEN + "0" + Fore.RED + " value given.")
        trash=input(Fore.RESET)
    else:
      print(Fore.RED + "ERROR: invalid ip '" + Fore.GREEN + str(ip_code)  + Fore.RED +  "'. Try Again" + Fore.RESET)
  else:
    if len(input_command) == 0:
      print(Fore.RED + "ERROR: invalid call. Try Again")
      print(Fore.RESET)
    else:    
      if input_command[0] == 'exit':
        
        print("")
        with console.status("[bold green]Processing...") as status:
          time.sleep(2)
        print("Exit Confirmed")
        
        def display_intro():
            time.sleep(1)
            console.print("[bold cyan]Thank you for using Task Vault[/bold cyan]", style="bold white")
            console.print("Preparing to delete data... Please wait.", style="bold green")
            time.sleep(1)

        def simulate_processing():
            with Progress(transient=True) as progress:
                task1 = progress.add_task("[cyan]Looping Data...", total=100)
                task2 = progress.add_task("[magenta]Processing Indents...", total=180)
                task3 = progress.add_task("[yellow]Finalizing...", total=100)

                while not progress.finished:
                    progress.update(task1, advance=random.randint(1, 10))
                    progress.update(task2, advance=random.randint(1, 10))
                    progress.update(task3, advance=random.randint(1, 10))
                    time.sleep(random.uniform(0.1, 0.3))

        def display_hacking_logs():
            logs = [
                "[bold green]Connected to: [yellow]192.168.1.1[/yellow][/bold green]",
                "[bold green]Accessing Database: [red]root{dir: main:[TaskVault.exe]}[/red][/bold green]",
                "[bold yellow]Bypassing Security Protocols...[/bold yellow]",
                "[bold yellow]Decrypting Data...[/bold yellow]",
                "[bold magenta]Data Deletion Complete.[/bold magenta]",
                "[bold cyan]Executing Cleanup Procedures...[/bold cyan]",
            ]
            
            for log in logs:
                console.print(log)
                time.sleep(random.uniform(1, 2))
        def simulate_network_activity():
            network_activity = [
                "[bold blue]Downloading update... 5%[/bold blue]",
                "[bold blue]Downloading update... 25%[/bold blue]",
                "[bold blue]Downloading update... 50%[/bold blue]",
                "[bold blue]Downloading update... 75%[/bold blue]",
                "[bold blue]Downloading update... 100%[/bold blue]",
                "[bold green]Update Complete.[/bold green]",
            ]
            
            for activity in network_activity:
                console.print(activity)
                time.sleep(random.uniform(0.5, 1.5))      
                
        display_intro()
        simulate_processing()
        display_hacking_logs()
        simulate_network_activity()
        print("")
        print(Fore.GREEN + "Ejection Successful!" + Fore.RESET)
        sys.exit()
      else:
        print(Fore.RED + "ERROR: invalid call. Try Again" + Fore.RESET)                             