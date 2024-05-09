play_data <- read.csv("C:\\Users\\jk121\\Documents\\Code\\learning-result\\大數據分析與應用\\0509\\DTree.csv", header = TRUE, sep = ",")

summary(play_data)

play_data

#=============================================================================
library(rpart)

play_DTree <- rpart(Play ~ ., 
                 data = play_data,
                 method = "class",
                 control = rpart.control(minsplit = 1),
                 parms = list(split = "information"))

summary(play_DTree)

#=============================================================================
