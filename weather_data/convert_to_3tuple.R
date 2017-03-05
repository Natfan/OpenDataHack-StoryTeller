#
#
# Encode lat lon forecast as a 3-tuple
#
#

d_lat <- 0.01
d_lon <- 0.01


lon_range <- c(-10,2)
lat_range <- c(4,61)

n_words <- 2000

# -------------------------------------------------

source("weather_classifications.R")

lat_coords <- seq(lat_range[[1]],lat_range[[2]],d_lat)
lon_coords <- seq(lon_range[[1]],lon_range[[2]],d_lon)
n_lats <- length(lat_coords)
n_lons <- length(lon_coords)

convert_3tuple <- function(input_file, n_words=7713) {
  
  indata <- read.csv(input_file)
  
  # Translate the weather data into a vector
  print(indata)
  f_temp <- function(i) { match(indata[["temperature"]][i], temp_band_names) }
  f_cloud <- function(i) { match(indata[["cloudcover"]][i], cloud_band_names) }
  f_wind <- function(i) { match(indata[["windspeed"]][i], wind_band_names) }
  f_precip <- function(i) { match(indata[["precip"]][i], all_precip_band_names) }
  n_times <- length(indata$lon)

  vector <- list(t2m = f_temp(1:n_times),
                 tcc = f_cloud(1:n_times),
                 ws = f_wind(1:n_times),
                 tp = f_precip(1:n_times))

  vector <- as.data.frame(vector)
  
  n_possibilities <- length(temp_band_names) *
    length(cloud_band_names) *
    length(wind_band_names) *
    length(all_precip_band_names)
  print(paste("Num possible forecasts = ",n_possibilities^length(vector[2,1]),sep=""))
  print(paste("Num coordinate locations = ",(n_lats*n_lons),sep=""))
  print(paste("Num forecast combinations = ",(n_lats*n_lons)*n_possibilities^length(vector[2,1]),sep=""))
  print(paste("Num word combinations = ",n_words^3))
  
  
}