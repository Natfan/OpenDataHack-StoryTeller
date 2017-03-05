#
#
# WEATHER CLASSIFICATIONS
#
#

temp_bands <- seq(-10,35,5)
n_tbands <- length(temp_bands)
temp_band_names <- c(paste("<",temp_bands[1]),
                     paste(temp_bands[1:n_tbands-1]," to ",temp_bands[2:n_tbands]),
                     paste(">",temp_bands[n_tbands]))

wind_bands <- c(5,15,20)
n_wbands <- length(wind_bands)
wind_band_names <- c("calm","gusty","gales","storm")

cloud_bands <- c(0.1,0.5,0.9)
n_cbands <- length(cloud_bands)
cloud_band_names <- c("clear","scattered clouds","cloudy","overcast")

precip_bands <- c(0.5,1,4,10)
snow_bands <- c(0.5)
n_pbands <- length(precip_bands)
precip_band_names <- c("dry","light rain","wet","heavy rain")
sleet_band_names  <- c("snow","sleet","sleet","heavy sleet")
