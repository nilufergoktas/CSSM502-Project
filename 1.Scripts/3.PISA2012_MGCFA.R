# CSSM502 - Fall 2022
# Nilüfer Göktaş, 49837
# Final Project - Investigating Measurement Invariance in PISA 2012

# Script 3 - Running Multi Group Confirmatory Factor Analysis (MGCFA) to test measurement invariance

install.packages("lavaan")
install.packages('semTools')
library(lavaan)
library(semTools)

pisadata <- read.csv("PISA2012_Cleaned.csv")
head(pisadata)
summary(pisadata)

tr = subset(pisadata, country == "TUR")
nld = subset(pisadata, country == "NLD")

###### MATH SELF EFFICACY ################################################################################################

# testing unidimentional model - FOR TURKEY
eff_mod <- 'selfefficacy =~ efficacy1 + efficacy2 + efficacy3 + efficacy4 + efficacy5 + efficacy6 + efficacy7 + efficacy8'
fit_eff_uni_TR<- cfa(eff_mod, data = tr, std.lv = T)
summary(fit_eff_uni_TR, fit.measures = T, standardized = T)

modindices(fit_eff_uni_TR, sort=T) # efficacy5 ~~ efficacy7

# testing MODIFIED unidimentional model - FOR TURKEY
eff_mod2 <-  'selfefficacy =~ efficacy1 + efficacy2 + efficacy3 + efficacy4 + efficacy5 + efficacy6 + efficacy7 + efficacy8
                     efficacy5 ~~ efficacy7 '
fit_eff_uni2_TR<- cfa(eff_mod2, data = tr, std.lv = T)
summary(fit_eff_uni2_TR, fit.measures = T, standardized = T)

# testing unidimentional model - FOR THE NETHERLANDS
eff_mod <- 'selfefficacy =~ efficacy1 + efficacy2 + efficacy3 + efficacy4 + efficacy5 + efficacy6 + efficacy7 + efficacy8'
fit_eff_uni_NLD<- cfa(eff_mod, data = nld, std.lv = T)
summary(fit_eff_uni_NLD, fit.measures = T, standardized = T)

modindices(fit_eff_uni_NLD, sort=T) # efficacy5 ~~ efficacy7

# testing (THE SAME) MODIFIED unidimentional model - FOR THE NETHERLANDS
eff_mod2 <-  'selfefficacy =~ efficacy1 + efficacy2 + efficacy3 + efficacy4 + efficacy5 + efficacy6 + efficacy7 + efficacy8
                     efficacy5 ~~ efficacy7 '
fit_eff_uni2_NLD<- cfa(eff_mod2, data = nld, std.lv = T)
summary(fit_eff_uni2_NLD, fit.measures = T, standardized = T)

###########################################################################################################################

# For the self efficacy measure, I will use the modified model for measurement invariance testing.

eff_mod2 <-  'selfefficacy =~ efficacy1 + efficacy2 + efficacy3 + efficacy4 + efficacy5 + efficacy6 + efficacy7 + efficacy8
                     efficacy5 ~~ efficacy7 '

# STEP 1. Configural Invariance
fit_eff_conf<-cfa(eff_mod2, data = pisadata, std.lv = T, group="country")
summary(fit_eff_conf, fit.measures=T, standardized = T)

# STEP 2. Metric Invariance
fit_eff_metric<-cfa(eff_mod2, data = pisadata, std.lv = T, group="country", group.equal = c("loadings"))
summary(fit_eff_metric, fit.measures=T, standardized = T)

# STEP 3. Scalar Invariance
fit_eff_scalar<-cfa(eff_mod2, data = pisadata, std.lv = T, group="country", group.equal = c("loadings","intercepts"))
summary(fit_eff_scalar, fit.measures=T, standardized = T)


###### MATH PERFORMANCE #################################################################################################

# testing unidimentional model - FOR TURKEY 
per_mod <- 'PVMATH =~ PVMATH1 + PVMATH2 + PVMATH3 + PVMATH4 + PVMATH5'
fit_per_uni_TR<- cfa(per_mod, data = tr, std.lv = T)
summary(fit_per_uni_TR, fit.measures = T, standardized = T)

# testing unidimentional model - FOR THE NETHERLANDS
per_mod <- 'PVMATH =~ PVMATH1 + PVMATH2 + PVMATH3 + PVMATH4 + PVMATH5'
fit_per_uni_NLD<- cfa(per_mod, data = nld, std.lv = T)
summary(fit_per_uni_NLD, fit.measures = T, standardized = T)

#########################################################################################################################

per_mod <- 'PVMATH =~ PVMATH1 + PVMATH2 + PVMATH3 + PVMATH4 + PVMATH5'

# STEP 1. Configural Invariance
fit_per_conf<-cfa(per_mod, data = pisadata, std.lv = T, group="country")
summary(fit_per_conf, fit.measures=T, standardized = T)

# STEP 2. Metric Invariance
fit_per_metric<-cfa(per_mod, data = pisadata, std.lv = T, group="country", group.equal = c("loadings"))
summary(fit_per_metric, fit.measures=T, standardized = T)

# STEP 3. Scalar Invariance
fit_per_scalar<-cfa(per_mod, data = pisadata, std.lv = T, group="country", group.equal = c("loadings","intercepts"))
summary(fit_per_scalar, fit.measures=T, standardized = T)
