import shutil
from pathlib import Path
import os

BACKUP_DIR = Path('backups/')
DATA_DIR = Path('data/')
EXPORT_DIR = Path('exports/')

def criar_diretorios():
    for directory in [BACKUP_DIR, DATA_DIR, EXPORT_DIR]:
        if not directory.exists():
            directory.mkdir(parents=True)

def fazer_backup():
    backup_file = BACKUP_DIR / f'backup_livraria_{data_atual()}.db'
    shutil.copy(DATA_DIR / 'livraria.db', backup_file)

def limpar_backups_antigos(max_backups=5):
    backups = sorted(BACKUP_DIR.glob('backup_livraria_*.db'), key=os.path.getmtime, reverse=True)
    for backup in backups[max_backups:]:
        backup.unlink()

def data_atual():
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d')
