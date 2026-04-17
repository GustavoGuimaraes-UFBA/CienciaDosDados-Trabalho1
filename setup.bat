@echo off
TITLE Configurando Ambiente Python

echo [1/3] Criando ambiente virtual (venv)...
python -m venv venv

if %errorlevel% neq 0 (
    echo.
    echo ERRO: O Python nao parece estar instalado ou no PATH do sistema.
    pause
    exit /b
)

echo [2/3] Ativando ambiente e instalando dependencias...
call venv\Scripts\activate && pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERRO: Falha ao instalar as dependencias. Verifique o arquivo requirements.txt.
    pause
    exit /b
)

echo [3/3] Tudo pronto! 
echo Para rodar seu script, lembre-se de sempre ativar o venv ou usar:
echo .\venv\Scripts\python.exe main.py
echo.
pause