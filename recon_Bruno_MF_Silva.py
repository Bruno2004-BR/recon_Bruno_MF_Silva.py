import platform
import os
import getpass
from datetime import datetime

# Função destinada à coleta de informações do sistema (T1082 - System Information Discovery)
def system_info_discovery():
    print("=== T1082 - System Information Discovery ===")
    # Obtém o hostname do sistema
    hostname = platform.node()
    print(f"Hostname: {hostname}")
    
    # Obtém o nome do sistema operacional
    os_name = platform.system()
    print(f"Sistema Operacional: {os_name}")
    
    # Obtém a versão do sistema operacional
    os_version = platform.release()
    print(f"Versão do SO: {os_version}")
    
    # Obtém a arquitetura do sistema
    architecture = platform.machine()
    print(f"Arquitetura: {architecture}")
    print()

# Função para obter informações do usuário (T1033 - User Account Discovery)
def user_account_discovery():
    print("=== T1033 - User Account Discovery ===")
    # Obtém o nome do usuário logado
    username = getpass.getuser()
    print(f"Usuário logado: {username}")
    
    # Consegue recuperar variáveis de ambiente úteis.
    useful_vars = ["USERPROFILE", "APPDATA"] if platform.system() == "Windows" else ["HOME", "PATH"]
    print("Variáveis de ambiente úteis:")
    for var in useful_vars:
        value = os.getenv(var)
        if value:
            print(f"{var}: {value}")
    print()

# Principal função para executar o script.
def main():
    print("Script de Reconhecimento - Simulação de Malware (MITRE ATT&CK)")
    print(f"Data/Hora: {datetime.now()}")
    print("=" * 50)
    
    # Realiza as tarefas de identificação.
    system_info_discovery()
    user_account_discovery()
    
    print("Simulação concluída. Este script foi criado para fins educacionais.")

if __name__ == "__main__":
    main() 