# Polynomial Linear regressing 多項式線性回歸:預測模型
![image](https://github.com/egroeglee/pictures/blob/master/PolynomialRegression/1.png)
![image](https://github.com/egroeglee/pictures/blob/master/PolynomialRegression/2.png)
 
         範例: 簡單的推測職位對應的薪水為多少
![image](https://github.com/egroeglee/pictures/blob/master/PolynomialRegression/3.png)

         注意: 
        1.因為資料量很小(只取Level欄位)，務必要把資料改為矩陣格式x = dataset.iloc[:, 1:2].values 以免資料無法計算
        2.又因為資料很少，我們想要建立的回歸模型需要把資料全部丟進去計算，不需要有訓練模型以及測試模型

         建立兩種模型: 線性回歸模型 / 多項式回歸模型
         1.Linear Regression
         2.Polynomial Regression
![image](https://github.com/egroeglee/pictures/blob/master/PolynomialRegression/4.png)![image](https://github.com/egroeglee/pictures/blob/master/PolynomialRegression/5.png)   

         第一欄為常數項 1  第三欄為平方 (也可以增加矩陣的位數，以增進較為完美的曲線

         輸出圖形:
         1.Linear Regression
![image](https://github.com/egroeglee/pictures/blob/master/PolynomialRegression/5.png) 

         2.Polynomial Regression
         A.矩陣設定為2時的曲線
![image](https://github.com/egroeglee/pictures/blob/master/PolynomialRegression/6.png)
![image](https://github.com/egroeglee/pictures/blob/master/PolynomialRegression/7.png)

         B.矩陣設定為4時的曲線
![image](https://github.com/egroeglee/pictures/blob/master/PolynomialRegression/8.png) 
         
         由上方兩圖中可以看出第二張圖的多項式回歸的預測線(矩陣為4)比較準確





       
