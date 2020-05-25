If you want to replace your NAs with a fixed value (a being your dataset):

a[is.na(a)] <- 0 #For instance
