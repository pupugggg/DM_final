# DM_final 第13組
B10715043王詠生

M10915033張鳴驛

M10915087徐逸安

M11015055王智優

# 實驗環境
## data summerization :
python 3.7
## gcluster1:
google colab
## gcluster2:
PyCharm Community Edition 2021.2.3
# 資料來源
Diamond9 & Cluto t4.8k
http://www2.cs.uh.edu/~ml_kdd/restored/Complex&Diamond/complex&diamond.htm
https://github.com/deric/clustering-benchmark/blob/master/src/main/resources/datasets/artificial/cluto-t4-8k.arff

# 操作說明
## data summerization :
1.資料格式
* 第一行請輸入屬性，後續放入資料
* 例:
   * x y class
   * 1 2 3
   * 2 3 4
   
2.操作方式
 * (1)將資料放入Data資料夾
 * (2)執行DataSum_main.py
 * (3)設置參數
 * 例:
    * 輸入主動變數屬性: **x y**
    * 輸入被動屬性: **z**
    * 輸入Epsilon: **50**
    * 輸入裝置數量: **1**
    * 輸入MinCells: **1**
    * 輸入MinForce: **1**
    * 輸入檔案名稱: **cluto-4k-8k.txt**
    * 輸入被動變數分段: **1 2 3**
 * (4)生成兩個檔案，分別為H_data.txt和original_data.txt。
    * 前者記錄了資料彙總後的三個參數: (1)cell座標 (2)mass center (3)data points數量
    * 後者記錄了可拿來做視覺化比對的三個參數: (1)原始資料 (2)該資料所屬cell (3)該資料在原資料集所屬label
 
## (gcluster1與gcluster2做的事情是一樣的，請選一個方便的方式執行)
### gcluster 1 :
請至 https://colab.research.google.com/drive/19ZffHy_9SDExAMUu06MR6tY26phSQpYW?hl=zh-tw#scrollTo=xwXY-rKoaNK8 或使用ipynb檔在google colab開啟，並將資料集放到google colab 預設資料夾中
### gcluster 2 :
1. 執行 main.py 程式。

2. 參數輸入。(參數如下)
* Diamond9:
  * 請輸入檔案: **H_data.txt** 
  * 請輸入 Cell Size: **30** 
  * 請輸入 Min Force: **0.0750**
  * 請輸入 Min Cells: **3**

* Cluto t4.8k:
  * 請輸入檔案: **H_data2.txt**
  * 請輸入 Cell Size: **50**
  * 請輸入 Min Force: **0.0845**
  * 請輸入 Min Cells: **3**
