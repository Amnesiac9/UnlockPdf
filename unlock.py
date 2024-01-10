import os
import pikepdf
import getpass

def unlock_pdf(filename, password):
    pdf = pikepdf.open(filename, password=password)
    pdf.save(filename.split('.pdf')[0] + '_unlocked.pdf')
    
    
files = os.listdir(os.getcwd())
# password = os.environ.get('password')
password = getpass.getpass(prompt='Enter password: ')

for file in files:
    if file.endswith('.pdf'):
        try:
            unlock_pdf(file, password)
            print(f'Unlocked {file}')
        except Exception as e:
            print(f'Error: {e}')