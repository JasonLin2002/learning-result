# Create the time series data
time_series_data <- c(120, 135, 150, 145, 155, 160, 162, 158, 165, 170)

# Convert the data into a time series object
ts_data <- ts(time_series_data)

# Plot the ACF up to lag 5
acf(ts_data, lag.max=5, main="ACF of Time Series Data up to Lag 5")

#==============================================================================
install.packages("forecast")
library(forecast)

# Create the time series data
time_series_data <- c(120, 135, 150, 145, 155, 160, 162, 158, 165, 170)

# Convert the data into a time series object
ts_data <- ts(time_series_data)

# Fit an MA model of order q
q <- 1
ma_model <- Arima(ts_data, order=c(0,0,q), include.mean=TRUE)

# Summary of the model
summary(ma_model)