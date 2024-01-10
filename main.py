import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

project_folder = os.path.dirname(os.path.realpath(__file__))
printables_folder = os.path.join(project_folder, "printables")
pdf_files = [file for file in os.listdir(
    printables_folder) if file.endswith(".pdf")]

print("Files in 'printables' folder:")
for file in pdf_files:
    print(file)

user_input = input(
    "Are these the files that you wish to print? (yes/no): ").lower()

if user_input == "yes":
    TF_ACCOUNT_NAME = os.getenv("TF_ACCOUNT_NAME")
    TF_ACCOUNT_PASSWORD = os.getenv("TF_ACCOUNT_PASSWORD")
    PRINTER_NAME = os.getenv("PRINTER_NAME")

    for file in pdf_files:
        scp_command = f"sshpass -p '{TF_ACCOUNT_PASSWORD}' scp {printables_folder}/{file} {TF_ACCOUNT_NAME}@login.informatik.uni-freiburg.de:~"
        subprocess.run(scp_command, shell=True, check=True)

        ssh_command = f"sshpass -p '{TF_ACCOUNT_PASSWORD}' ssh {TF_ACCOUNT_NAME}@login.informatik.uni-freiburg.de "
        lpr_command = f"lp -o sides=one-sided {file} -d {PRINTER_NAME}"

        subprocess.run(ssh_command + lpr_command, shell=True, check=True)

        lpq_command = f"{ssh_command} lpq -P {PRINTER_NAME}"
        lpq_result = subprocess.run(
            lpq_command, shell=True, capture_output=True, text=True)

        print("\nlpq result:")
        print(lpq_result.stdout)

        subprocess.run(f"{ssh_command} exit", shell=True, check=True)

    print("\nPrint job completed.")
else:
    print("Printing canceled.")
