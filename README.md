# English :us:
# Automatic Backup Script

This Python script is designed to perform automatic backups of files or directories at regular intervals. The backups are saved in a destination folder with a unique name based on a timestamp.

## Features:
- Automatically copies files or directories from a specified source to a destination.
- Each backup is saved in a unique folder with a timestamp (e.g., `backup_20241214_153000`).
- The backup process runs at regular intervals (configurable).
- Easy to set up and use with minimal configuration.

## Requirements:
- Python 3.x
- `shutil` and `os` libraries (included by default in Python)

## Installation:
1. Clone this repository or download the script to your local machine.
2. Ensure you have Python 3.x installed.
3. Install any dependencies (if needed) using `pip` (though the script should run with the default Python installation).

## Configuration:
To use the script, you'll need to configure the following variables in the code:

1. **source:** The path to the directory or file you want to back up. Replace `'path/to/your/source_directory_or_file'` with the actual path.
2. **destination:** The path to the directory where the backups will be stored. Replace `'path/to/your/backup_directory'` with the actual backup destination.
3. **interval_seconds:** The time interval between backups, in seconds. For example, setting it to `3600` will perform backups every hour.

## Usage:

1. Modify the `source`, `destination`, and `interval_seconds` variables in the script to fit your needs.
2. Run the script. It will start making backups at the specified intervals.
3. The script will continue to run indefinitely, making backups at the specified interval, until manually stopped.

### Example:
If you want to back up a folder `my_folder` to a backup directory `my_backups` every 2 hours (7200 seconds), set:
```python
source = 'path/to/my_folder'
destination = 'path/to/my_backups'
interval_seconds = 7200
```
---
# Português :brazil:
# Script de Backup Automático

Este script em Python foi projetado para realizar backups automáticos de arquivos ou diretórios em intervalos regulares. Os backups são salvos em uma pasta de destino com um nome único baseado em um timestamp.

## Características:
- Copia automaticamente arquivos ou diretórios de uma origem especificada para um destino.
- Cada backup é salvo em uma pasta única com um timestamp (por exemplo, `backup_20241214_153000`).
- O processo de backup é executado em intervalos regulares (configuráveis).
- Fácil de configurar e usar com configuração mínima.

## Requisitos:
- Python 3.x
- Bibliotecas `shutil` e `os` (incluídas por padrão no Python)

## Instalação:
1. Clone este repositório ou baixe o script para sua máquina local.
2. Certifique-se de ter o Python 3.x instalado.
3. Instale as dependências necessárias (se houver) usando `pip` (embora o script deva funcionar com a instalação padrão do Python).

## Configuração:
Para usar o script, você precisará configurar as seguintes variáveis no código:

1. **source:** O caminho para o diretório ou arquivo que você deseja fazer o backup. Substitua `'path/to/your/source_directory_or_file'` pelo caminho real.
2. **destination:** O caminho para o diretório onde os backups serão armazenados. Substitua `'path/to/your/backup_directory'` pelo caminho real de destino.
3. **interval_seconds:** O intervalo de tempo entre os backups, em segundos. Por exemplo, configurá-lo para `3600` fará o backup a cada hora.

## Uso:

1. Modifique as variáveis `source`, `destination` e `interval_seconds` no script conforme necessário.
2. Execute o script. Ele começará a fazer backups nos intervalos especificados.
3. O script continuará a ser executado indefinidamente, fazendo backups nos intervalos especificados, até ser interrompido manualmente.

### Exemplo:
Se você deseja fazer backup de uma pasta `my_folder` para um diretório de backups `my_backups` a cada 2 horas (7200 segundos), configure:
```python
source = 'path/to/my_folder'
destination = 'path/to/my_backups'
interval_seconds = 7200
```
