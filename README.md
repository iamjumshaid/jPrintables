# Print Automation Script

This script automates the process of transferring PDF files to a remote server and printing them using SSH. It uses environment variables from a `.env` file for configuration.

## Prerequisites

- Python 3
- `sshpass` (install using your system's package manager, e.g., `brew install hudochenkov/sshpass/sshpass` on macOS) (`sudo apt-get install sshpass` on Linux
)

## Setup

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the project root with the following content:

    ```plaintext
    TF_ACCOUNT_NAME=your_tf_account_name
    TF_ACCOUNT_PASSWORD=your_tf_account_password
    PRINTER_NAME=your_printer_name
    ```

## Usage

1. Place the PDF files you want to print in the `printables` folder.

2. Run the script:

    ```bash
    python main.py
    ```

3. Follow the prompts to confirm the files for printing.

4. The script will transfer the files, print them, show the print queue status, and then complete the print job.

