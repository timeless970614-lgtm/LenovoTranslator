@echo off
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
LunaTranslator.exe -S -c "import sys,os;sys.path.insert(0,'LunaTranslator');sys.path.insert(1,'userconfig');_f='LunaTranslator/main.py';exec(compile(open(_f,encoding='utf-8').read(),os.path.abspath(_f),'exec'),{'__file__':os.path.abspath(_f),'__name__':'__main__','__builtins__':__builtins__,'__doc__':None,'__loader__':None,'__spec__':None,'__package__':None,'__cached__':None})" %*