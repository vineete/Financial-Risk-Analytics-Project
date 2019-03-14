library(survival)
library(survminer)
library(plotly)

mydata <- read.csv("processed_hazard.csv")

mydata <- subset(mydata, select = -c(1))

# Iterate through with different single variables (univariate case)
# Compare results to multivariate case shown later on
first_model <- coxph(Surv(T.t0.years., value) ~ unemp_t, data = mydata)
summary(first_model)

#Multivariate (incorporate all features)
mult_model <- coxph(Surv(T.t0.years., value) ~ . , data =  mydata)
summary(mult_model)

### Save relevant plots to disk

png(file = "multi_plot.png")
ggsurvplot(survfit(mult_model), legend = "none",palette = "#2E9FDF",ggtheme = theme_minimal(),title = "Multivariate hazard model",ylim = c(0.9,1),data = mydata)
dev.off()


png(file = "sample_uni_plot.png")
ggsurvplot(survfit(first_model),legend = "none", palette = "#2E9FDF",ggtheme = theme_minimal(),title = "Univariate hazard model (unemployment)",ylim = c(0.9,1),data = adjust_data)
dev.off()


### Sensitivity Analysis
adjust_data <- mydata
adjust_data$unemp_t = adjust_data$unemp_t*2
adjusted_model <-survfit(mult_model,adjust_data)
extract = adjusted_model$surv[0:48]

#png(file = "2X-unemployment.png")
plot(extract,type = "l", col = "red", xlab = "Time (Years)", ylab = "Probability of Survival",
     main = "Survival Probability (Unemployment Rate 2Xed)")
#dev.off()
#ggsurvplot(adjusted_model, legend = "none",palette = "#2E9FDF",ggtheme = theme_minimal(),title = "Multivariate hazard model",ylim = c(0.9,1),data = adjust_data)


### Obtain Probabilities

prob_data <- read.csv("prob_file.csv")
splitted <- split(prob_data,f = prob_data$LoanNum)

len = 497
final_prob_df <- data.frame(matrix(NA, nrow = len, ncol = 3))
for (i in 1:len) {
  temp <- splitted[[i]]
  loan_number <-temp$LoanNum[1]
  final_prob_df[i,1] = loan_number
  temp <- subset(temp, select = -c(1,24)) 
  temp2 <- temp[names(adjust_data)]
  new_model <-survfit(mult_model,temp2)
  one_prob = new_model$surv[1]
  five_prob = new_model$surv[5]
  final_prob_df[i,2] = one_prob
  final_prob_df[i,3] = five_prob
}

write.csv(final_prob_df, file = "probabilities.csv")
