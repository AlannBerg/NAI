# Gomboku
Simple python AI game, created to pass NAI subject on PJATK


The board positions are numbered row + column. Board is 15x15:
```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 
10 11 12 13 14 15 16 17 18 19 110 111 112 113 114 
20 21 22 23 24 25 26 27 28 29 210 211 212 213 214 
30 31 32 33 34 35 36 37 38 39 310 311 312 313 314 
40 41 42 43 44 45 46 47 48 49 410 411 412 413 414 
50 51 52 53 54 55 56 57 58 59 510 511 512 513 514 
60 61 62 63 64 65 66 67 68 69 610 611 612 613 614 
70 71 72 73 74 75 76 77 78 79 710 711 712 713 714 
80 81 82 83 84 85 86 87 88 89 810 811 812 813 814 
90 91 92 93 94 95 96 97 98 99 910 911 912 913 914 
100 101 102 103 104 105 106 107 108 109 1010 1011 1012 1013 1014 
110 111 112 113 114 115 116 117 118 119 1110 1111 1112 1113 1114 
120 121 122 123 124 125 126 127 128 129 1210 1211 1212 1213 1214 
130 131 132 133 134 135 136 137 138 139 1310 1311 1312 1313 1314 
140 141 142 143 144 145 146 147 148 149 1410 1411 1412 1413 1414  
```
Created by: Alan Berg && Tomasz Fidurski.

In Gomoku to win a game player have to placehis 5 pointers next to each other in : 
row, column, diagonally

To choose a cell user have to type in terminal (x, y) for example for field 5,5
(5, 5)

By default user mark is ``` B ``` Black
AI mark is ```W ``` White

By default first move is for user. If you want AI to make first move you have to change line ``` self.current_player = 1 ``` to ``` self.current_player = 2``` 

User can choose difficult level by changing value of ```ai_algo ```. By default it is easy_ai. Negamax() means how many moves in advance ai considers

In 

``` #How many steps will AI think in advance
easy_ai = Negamax(2)
medium_ai = Negamax(4)
hard_ai = Negamax(6)

#Choose difficult level
ai_algo = easy_ai
```

## How to instal:
1) ``` git clone https://github.com/AlannBerg/Gomboku.git```
2) ```pip install easyai```
3) ```pip install tabulate```
4) ``` python .\Gomoku-2D.py ```

## Example gameplay photos
<img width="714" alt="image" src="https://github.com/AlannBerg/Gomboku/assets/76206945/b24aa8c9-7748-4aad-a739-f840d5ef855b">
<img width="828" alt="image" src="https://github.com/AlannBerg/Gomboku/assets/76206945/228137ff-d5b7-4fb8-8503-aa286c03772c">

