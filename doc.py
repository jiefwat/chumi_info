我有一个库存优化的excel表 10行，以第一行举例，每列的字段是
A列：零件成本
B列：零件的月需求
C列：提前期天数
F列：库存
D列：B2/30*C2
E列：D2/SUM(D2：D11)
G列：F2*A2
H列：POISSON(F2,B2/30*C2,1)
i列：D2*H2
j列：POISSON(F2+1,B2/30*C2,TRUE)
k列：(SUM(I2:I11)-I2+J2*D2)/SUM(D2:D11)
l列：(K2-I12)/A2