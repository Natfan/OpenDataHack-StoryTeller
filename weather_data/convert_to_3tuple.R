#
#
# Encode lat lon forecast as a 3-tuple
#
#

source("weather_classifications.R")

convert_3tuple <- function(input_file, n_words=7713) {
  
  indata <- read.csv(input_file)
  
  # Translate the weather data into a vector
  print(head(indata))
  f_temp <- function(i) { match(indata$temperature[i], temp_band_names) }
  n_times <- length(indata$lon)
  print(f_temp(1:n_times))
  vector <- list(t2m = temp_bands[f_temp(1:n_times)])

  print(vector)
}