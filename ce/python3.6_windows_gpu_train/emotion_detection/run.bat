@echo off
set models_dir=./../../models_repo
rem copy models files
xcopy "%models_dir%/PaddleNLP/emotion_detection/." . /s /e /y
if not exist data (mklink /j data %data_path%\emotion_detection\data)
if not exist models (mklink /j models %data_path%\emotion_detection\models)
.\.run_ce.bat
