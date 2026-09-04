\# DAX Mesures  



** Attrition Rate** 



```DAX

Attrition Rate= 

DIVIDE(

&#x20;   CALCULATE(

&#x20;       COUNTROWS('WA\_Fn-UseC\_-HR-Employee-Attrition'),

&#x20;       'WA\_Fn-UseC\_-HR-Employee-Attrition'\[Attrition] = "Yes"

&#x20;   ),

&#x20;   COUNTROWS('WA\_Fn-UseC\_-HR-Employee-Attrition'),

&#x20;   0

)





** AVG Income** 



```DAX

AVG Income= 

AVERAGE('WA\_Fn-UseC\_-HR-Employee-Attrition'\[MonthlyIncome])







** OverTime Employees Attrition**



```DAX

OverTime Employees Attrition = 

DIVIDE(

&#x20;   CALCULATE(

&#x20;       COUNTROWS('WA\_Fn-UseC\_-HR-Employee-Attrition'),

&#x20;       'WA\_Fn-UseC\_-HR-Employee-Attrition'\[Attrition] = "Yes",

&#x20;       'WA\_Fn-UseC\_-HR-Employee-Attrition'\[OverTime] = "Yes"

&#x20;   ),

&#x20;   CALCULATE(

&#x20;       COUNTROWS('WA\_Fn-UseC\_-HR-Employee-Attrition'),

&#x20;       'WA\_Fn-UseC\_-HR-Employee-Attrition'\[OverTime] = "Yes"

&#x20;   ),

&#x20;   0

)





**Total Working Years - Attrition**



```DAX

Total Working Years - Attrition = 

CALCULATE(

&#x20;   AVERAGE('WA\_Fn-UseC\_-HR-Employee-Attrition'\[YearsAtCompany]),

&#x20;   'WA\_Fn-UseC\_-HR-Employee-Attrition'\[Attrition]= "Yes")

