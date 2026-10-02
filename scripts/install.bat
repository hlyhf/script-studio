@echo off
rem 安装 script-studio 技能到 Hermes Agent skills 目录 (Windows)
rem 用法: install.bat [目标skills目录]   默认: %USERPROFILE%\.hermes\skills
setlocal
set "REPO_ROOT=%~dp0.."
set DEST=%USERPROFILE%\.hermes\skills
if not "%~1"=="" set DEST=%~1
if not exist "%DEST%" mkdir "%DEST%"
if exist "%DEST%\script-studio" rmdir /s /q "%DEST%\script-studio"
xcopy /E /I /Q "%REPO_ROOT%\skill\script-studio" "%DEST%\script-studio" >nul
echo [OK] script-studio 已安装到 %DEST%\script-studio
echo      重启 Hermes Agent 会话后自动可用
endlocal
