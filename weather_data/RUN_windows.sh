#!/bin/bash

RSCRIPT="~/../../Program Files/R/R-3.3.2/bin/Rscript.exe"
# RSCRIPT="./Rscript.exe"

if [ -f "temp_input.txt" ]
then 
	rm "temp_input.txt"
fi

~/../../Program\ Files/R/R-3.3.2/bin/Rscript.exe set_up_weather_data_download.R

python get_weather_data.py

~/../../Program\ Files/R/R-3.3.2/bin/Rscript.exe extract_data.R	
