@echo off
cd /d "%~dp0"
python 2_generate_data.py
python 3_load_data.py
python 4_clean_data.py
python 5_merge_data.py
python 6_calculate_performance.py
python 7_store_results.py
python 8_visualize_data.py
echo All scripts executed successfully!
pause
