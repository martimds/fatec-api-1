chcp 65001
@echo off

IF NOT EXIST .venv (
    echo Criando ambiente virtual...
    python -m venv .venv
)

echo Ativando ambiente virtual...
call .venv\Scripts\activate

pip show Flask >nul 2>nul
IF ERRORLEVEL 1 (
    echo Instalando Flask...
    pip install Flask
) else (
    echo Flask já está instalado.
)

echo Executando app.py...
cd src
python app.py

