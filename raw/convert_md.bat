@echo off
setlocal enabledelayedexpansion

REM このスクリプトのディレクトリを取得
set SCRIPT_DIR=%~dp0

REM Pythonスクリプトのパス
set PYTHON_SCRIPT=%SCRIPT_DIR%convert_md.py

REM 出力ディレクトリ
set OUTPUT_DIR=%SCRIPT_DIR%..\content

REM 出力ディレクトリが存在しない場合は作成
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

REM カレントディレクトリの.mdファイルをすべて処理
for %%f in (*.md) do (
    python "%PYTHON_SCRIPT%" "%%f" "%OUTPUT_DIR%\%%f"
)

echo Conversion complete.
pause
