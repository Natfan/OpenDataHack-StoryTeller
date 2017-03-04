# Extract data from a netcdf file

require(RNetCDF)

#lat <- 51.449
#lon <- -0.958

#filename <- "temp.nc"
#var <- "t2m"

#----------------------------

GetPointDataNetCDF <- function(filename, lat, lon, var) {

  if(lon < 0) { lon <- lon+360 }
  
  data <- open.nc(filename,write=FALSE)
  x <- read.nc(data)
  
  if(var.inq.nc(ncfile = data,var=0)$name != "longitude") {
    stop("Longitude data not found :O")
  }
  if(var.inq.nc(ncfile = data,var=1)$name != "latitude") {
    stop("Latitude data not found :O")
  }
  #if(var.inq.nc(ncfile = data,var=5)$name != "t2m") {
  #  stop("2m temp not found :O")
  #}
  
  nc_lon <- x[[1]]  # longitude
  nc_lat <- x[[2]]  # latitude
  
  lat_ind <- which.min(abs(lat-nc_lat)) # index closest to input lon
  lon_ind <- which.min(abs(lon-nc_lon)) # index closest to input lat
  
  out <- list()
  
  for (i in 3:length(x)) {
    varname <- var.inq.nc(ncfile = data,var=(i-1))$name
    print(paste("Looking at ",varname,sep=""))
    print(var %in% varname)
    if (var %in% varname) {
      var_data <- x[[i]]                       # nc data
      var_ts   <- var_data[lon_ind,lat_ind,]
      out[[var]] <- var_ts
    }
  }
  
  return(out)
}