import tkinter as tk
import os
import time
from sys import exit

# initializarea variabilelor globale
i = 1
scor = 0
coloana_scor = 0
NUME = ""
PRENUME = ""
VARSTA = 0
timp_final = 0
text_rezultat = ""
RASPUNS = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

BAREM = [[4, 5, 1, 2, 6, 3, 6, 2, 1, 3, 4, 5],
         [2, 6, 1, 2, 1, 3, 5, 6, 4, 3, 4, 5],
         [8, 2, 3, 8, 7, 4, 5, 1, 7, 6, 1, 2],
         [3, 4, 3, 7, 8, 6, 5, 4, 1, 2, 5, 6],
         [7, 6, 8, 2, 1, 5, 1, 6, 3, 2, 4, 5]]

REZULTATE = [[73, 65, 57, 53, 48, 48, 46, 0],
             [74, 67, 58, 54, 49, 48, 47, 0],
             [76, 68, 60, 55, 51, 49, 49, 0],
             [77, 70, 61, 57, 52, 50, 50, 0],
             [79, 71, 63, 58, 53, 52, 51, 0],
             [81, 73, 64, 59, 55, 53, 52, 0],
             [82, 74, 66, 61, 56, 54, 54, 0],
             [84, 76, 67, 62, 57, 55, 55, 0],
             [85, 77, 69, 64, 59, 57, 56, 0],
             [87, 79, 70, 65, 60, 58, 57, 55],
             [89, 80, 72, 66, 61, 59, 59, 57],
             [90, 82, 73, 67, 64, 60, 60, 58],

             [92, 83, 75, 68, 64, 62, 61, 59],
             [93, 84, 76, 69, 65, 63, 62, 61],
             [95, 86, 78, 72, 67, 64, 64, 62],
             [97, 88, 79, 73, 68, 66, 65, 65],
             [98, 89, 81, 75, 69, 67, 66, 65],
             [100, 91, 82, 76, 71, 68, 67, 66],
             [101, 92, 84, 78, 72, 69, 69, 67],
             [103, 94, 85, 79, 73, 71, 70, 69],
             [104, 95, 87, 80, 75, 72, 71, 70],
             [105, 97, 88, 82, 76, 73, 72, 71],
             [107, 98, 90, 83, 77, 74, 74, 72],
             [108, 100, 91, 85, 79, 76, 75, 74],

             [109, 101, 93, 86, 80, 77, 76, 75],
             [110, 103, 94, 87, 81, 78, 77, 76],
             [112, 104, 96, 89, 83, 80, 79, 78],
             [113, 106, 97, 90, 83, 81, 80, 79],
             [114, 107, 99, 92, 85, 82, 81, 80],
             [116, 109, 100, 93, 87, 83, 82, 82],
             [117, 110, 102, 94, 88, 85, 84, 83],
             [118, 112, 103, 96, 89, 86, 85, 84],
             [120, 113, 104, 97, 91, 87, 86, 86],
             [121, 115, 105, 99, 92, 88, 87, 87],
             [122, 116, 107, 100, 93, 90, 89, 88],
             [123, 118, 109, 102, 95, 91, 90, 90],

             [125, 119, 110, 104, 96, 92, 91, 91],
             [126, 121, 112, 105, 97, 94, 92, 92],
             [127, 122, 113, 107, 99, 95, 94, 94],
             [129, 124, 115, 109, 100, 96, 95, 95],
             [130, 125, 117, 111, 102, 97, 96, 96],
             [131, 127, 118, 112, 104, 99, 97, 98],
             [132, 128, 120, 114, 106, 100, 99, 99],
             [134, 130, 121, 116, 108, 102, 100, 100],
             [135, 131, 123, 118, 110, 105, 102, 102],
             [136, 133, 125, 120, 112, 107, 105, 104],
             [138, 134, 126, 121, 114, 109, 107, 106],
             [139, 136, 128, 123, 116, 111, 110, 108],

             [140, 137, 129, 125, 118, 114, 112, 110],
             [142, 139, 131, 127, 120, 116, 115, 112],
             [143, 140, 133, 128, 122, 118, 117, 114],
             [144, 142, 134, 130, 124, 121, 120, 116],
             [146, 143, 136, 132, 126, 123, 122, 118],
             [147, 145, 137, 134, 128, 125, 123, 120],
             [148, 146, 139, 136, 130, 127, 127, 122],
             [149, 148, 140, 137, 132, 130, 130, 124],
             [151, 149, 142, 139, 134, 132, 132, 126],
             [152, 151, 144, 141, 136, 134, 134, 128],
             [153, 152, 145, 143, 138, 137, 137, 130],
             [155, 154, 147, 144, 140, 139, 139, 130]]

INTREBARI = {
    1: ["Poze/A1.png", "Poze/A1_1.png", "Poze/A1_2.png", "Poze/A1_3.png",
        "Poze/A1_4.png", "Poze/A1_5.png", "Poze/A1_6.png"],
    2: ["Poze/A2.png", "Poze/A2_1.png", "Poze/A2_2.png", "Poze/A2_3.png",
        "Poze/A2_4.png", "Poze/A2_5.png", "Poze/A2_6.png"],
    3: ["Poze/A3.png", "Poze/A3_1.png", "Poze/A3_2.png", "Poze/A3_3.png",
        "Poze/A3_4.png", "Poze/A3_5.png", "Poze/A3_6.png"],
    4: ["Poze/A4.png", "Poze/A4_1.png", "Poze/A4_2.png", "Poze/A4_3.png",
        "Poze/A4_4.png", "Poze/A4_5.png", "Poze/A4_6.png"],
    5: ["Poze/A5.png", "Poze/A5_1.png", "Poze/A5_2.png", "Poze/A5_3.png",
        "Poze/A5_4.png", "Poze/A5_5.png", "Poze/A5_6.png"],
    6: ["Poze/A6.png", "Poze/A6_1.png", "Poze/A6_2.png", "Poze/A6_3.png",
        "Poze/A6_4.png", "Poze/A6_5.png", "Poze/A6_6.png"],
    7: ["Poze/A7.png", "Poze/A7_1.png", "Poze/A7_2.png", "Poze/A7_3.png",
        "Poze/A7_4.png", "Poze/A7_5.png", "Poze/A7_6.png"],
    8: ["Poze/A8.png", "Poze/A8_1.png", "Poze/A8_2.png", "Poze/A8_3.png",
        "Poze/A8_4.png", "Poze/A8_5.png", "Poze/A8_6.png"],
    9: ["Poze/A9.png", "Poze/A9_1.png", "Poze/A9_2.png", "Poze/A9_3.png",
        "Poze/A9_4.png", "Poze/A9_5.png", "Poze/A9_6.png"],
    10: ["Poze/A10.png", "Poze/A10_1.png", "Poze/A10_2.png", "Poze/A10_3.png",
         "Poze/A10_4.png", "Poze/A10_5.png", "Poze/A10_6.png"],
    11: ["Poze/A11.png", "Poze/A11_1.png", "Poze/A11_2.png", "Poze/A11_3.png",
         "Poze/A11_4.png", "Poze/A11_5.png", "Poze/A11_6.png"],
    12: ["Poze/A12.png", "Poze/A12_1.png", "Poze/A12_2.png", "Poze/A12_3.png",
         "Poze/A12_4.png", "Poze/A12_5.png", "Poze/A12_6.png"],

    13: ["Poze/B1.png", "Poze/B1_1.png", "Poze/B1_2.png", "Poze/B1_3.png",
         "Poze/B1_4.png", "Poze/B1_5.png", "Poze/B1_6.png"],
    14: ["Poze/B2.png", "Poze/B2_1.png", "Poze/B2_2.png", "Poze/B2_3.png",
         "Poze/B2_4.png", "Poze/B2_5.png", "Poze/B2_6.png"],
    15: ["Poze/B3.png", "Poze/B3_1.png", "Poze/B3_2.png", "Poze/B3_3.png",
         "Poze/B3_4.png", "Poze/B3_5.png", "Poze/B3_6.png"],
    16: ["Poze/B4.png", "Poze/B4_1.png", "Poze/B4_2.png", "Poze/B4_3.png",
         "Poze/B4_4.png", "Poze/B4_5.png", "Poze/B4_6.png"],
    17: ["Poze/B5.png", "Poze/B5_1.png", "Poze/B5_2.png", "Poze/B5_3.png",
         "Poze/B5_4.png", "Poze/B5_5.png", "Poze/B5_6.png"],
    18: ["Poze/B6.png", "Poze/B6_1.png", "Poze/B6_2.png", "Poze/B6_3.png",
         "Poze/B6_4.png", "Poze/B6_5.png", "Poze/B6_6.png"],
    19: ["Poze/B7.png", "Poze/B7_1.png", "Poze/B7_2.png", "Poze/B7_3.png",
         "Poze/B7_4.png", "Poze/B7_5.png", "Poze/B7_6.png"],
    20: ["Poze/B8.png", "Poze/B8_1.png", "Poze/B8_2.png", "Poze/B8_3.png",
         "Poze/B8_4.png", "Poze/B8_5.png", "Poze/B8_6.png"],
    21: ["Poze/B9.png", "Poze/B9_1.png", "Poze/B9_2.png", "Poze/B9_3.png",
         "Poze/B9_4.png", "Poze/B9_5.png", "Poze/B9_6.png"],
    22: ["Poze/B10.png", "Poze/B10_1.png", "Poze/B10_2.png", "Poze/B10_3.png",
         "Poze/B10_4.png", "Poze/B10_5.png", "Poze/B10_6.png"],
    23: ["Poze/B11.png", "Poze/B11_1.png", "Poze/B11_2.png", "Poze/B11_3.png",
         "Poze/B11_4.png", "Poze/B11_5.png", "Poze/B11_6.png"],
    24: ["Poze/B12.png", "Poze/B12_1.png", "Poze/B12_2.png", "Poze/B12_3.png",
         "Poze/B12_4.png", "Poze/B12_5.png", "Poze/B12_6.png"],

    25: ["Poze/C1.png", "Poze/C1_1.png", "Poze/C1_2.png", "Poze/C1_3.png", "Poze/C1_4.png",
         "Poze/C1_5.png", "Poze/C1_6.png", "Poze/C1_7.png", "Poze/C1_8.png"],
    26: ["Poze/C2.png", "Poze/C2_1.png", "Poze/C2_2.png", "Poze/C2_3.png", "Poze/C2_4.png",
         "Poze/C2_5.png", "Poze/C2_6.png", "Poze/C2_7.png", "Poze/C2_8.png"],
    27: ["Poze/C3.png", "Poze/C3_1.png", "Poze/C3_2.png", "Poze/C3_3.png", "Poze/C3_4.png",
         "Poze/C3_5.png", "Poze/C3_6.png", "Poze/C3_7.png", "Poze/C3_8.png"],
    28: ["Poze/C4.png", "Poze/C4_1.png", "Poze/C4_2.png", "Poze/C4_3.png", "Poze/C4_4.png",
         "Poze/C4_5.png", "Poze/C4_6.png", "Poze/C4_7.png", "Poze/C4_8.png"],
    29: ["Poze/C5.png", "Poze/C5_1.png", "Poze/C5_2.png", "Poze/C5_3.png", "Poze/C5_4.png",
         "Poze/C5_5.png", "Poze/C5_6.png", "Poze/C5_7.png", "Poze/C5_8.png"],
    30: ["Poze/C6.png", "Poze/C6_1.png", "Poze/C6_2.png", "Poze/C6_3.png", "Poze/C6_4.png",
         "Poze/C6_5.png", "Poze/C6_6.png", "Poze/C6_7.png", "Poze/C6_8.png"],
    31: ["Poze/C7.png", "Poze/C7_1.png", "Poze/C7_2.png", "Poze/C7_3.png", "Poze/C7_4.png",
         "Poze/C7_5.png", "Poze/C7_6.png", "Poze/C7_7.png", "Poze/C7_8.png"],
    32: ["Poze/C8.png", "Poze/C8_1.png", "Poze/C8_2.png", "Poze/C8_3.png", "Poze/C8_4.png",
         "Poze/C8_5.png", "Poze/C8_6.png", "Poze/C8_7.png", "Poze/C8_8.png"],
    33: ["Poze/C9.png", "Poze/C9_1.png", "Poze/C9_2.png", "Poze/C9_3.png", "Poze/C9_4.png",
         "Poze/C9_5.png", "Poze/C9_6.png", "Poze/C9_7.png", "Poze/C9_8.png"],
    34: ["Poze/C10.png", "Poze/C10_1.png", "Poze/C10_2.png", "Poze/C10_3.png", "Poze/C10_4.png",
         "Poze/C10_5.png", "Poze/C10_6.png", "Poze/C10_7.png", "Poze/C10_8.png"],
    35: ["Poze/C11.png", "Poze/C11_1.png", "Poze/C11_2.png", "Poze/C11_3.png", "Poze/C11_4.png",
         "Poze/C11_5.png", "Poze/C11_6.png", "Poze/C11_7.png", "Poze/C11_8.png"],
    36: ["Poze/C12.png", "Poze/C12_1.png", "Poze/C12_2.png", "Poze/C12_3.png", "Poze/C12_4.png",
         "Poze/C12_5.png", "Poze/C12_6.png", "Poze/C12_7.png", "Poze/C12_8.png"],

    37: ["Poze/D1.png", "Poze/D1_1.png", "Poze/D1_2.png", "Poze/D1_3.png", "Poze/D1_4.png",
         "Poze/D1_5.png", "Poze/D1_6.png", "Poze/D1_7.png", "Poze/D1_8.png"],
    38: ["Poze/D2.png", "Poze/D2_1.png", "Poze/D2_2.png", "Poze/D2_3.png", "Poze/D2_4.png",
         "Poze/D2_5.png", "Poze/D2_6.png", "Poze/D2_7.png", "Poze/D2_8.png"],
    39: ["Poze/D3.png", "Poze/D3_1.png", "Poze/D3_2.png", "Poze/D3_3.png", "Poze/D3_4.png",
         "Poze/D3_5.png", "Poze/D3_6.png", "Poze/D3_7.png", "Poze/D3_8.png"],
    40: ["Poze/D4.png", "Poze/D4_1.png", "Poze/D4_2.png", "Poze/D4_3.png", "Poze/D4_4.png",
         "Poze/D4_5.png", "Poze/D4_6.png", "Poze/D4_7.png", "Poze/D4_8.png"],
    41: ["Poze/D5.png", "Poze/D5_1.png", "Poze/D5_2.png", "Poze/D5_3.png", "Poze/D5_4.png",
         "Poze/D5_5.png", "Poze/D5_6.png", "Poze/D5_7.png", "Poze/D5_8.png"],
    42: ["Poze/D6.png", "Poze/D6_1.png", "Poze/D6_2.png", "Poze/D6_3.png", "Poze/D6_4.png",
         "Poze/D6_5.png", "Poze/D6_6.png", "Poze/D6_7.png", "Poze/D6_8.png"],
    43: ["Poze/D7.png", "Poze/D7_1.png", "Poze/D7_2.png", "Poze/D7_3.png", "Poze/D7_4.png",
         "Poze/D7_5.png", "Poze/D7_6.png", "Poze/D7_7.png", "Poze/D7_8.png"],
    44: ["Poze/D8.png", "Poze/D8_1.png", "Poze/D8_2.png", "Poze/D8_3.png", "Poze/D8_4.png",
         "Poze/D8_5.png", "Poze/D8_6.png", "Poze/D8_7.png", "Poze/D8_8.png"],
    45: ["Poze/D9.png", "Poze/D9_1.png", "Poze/D9_2.png", "Poze/D9_3.png", "Poze/D9_4.png",
         "Poze/D9_5.png", "Poze/D9_6.png", "Poze/D9_7.png", "Poze/D9_8.png"],
    46: ["Poze/D10.png", "Poze/D10_1.png", "Poze/D10_2.png", "Poze/D10_3.png", "Poze/D10_4.png",
         "Poze/D10_5.png", "Poze/D10_6.png", "Poze/D10_7.png", "Poze/D10_8.png"],
    47: ["Poze/D11.png", "Poze/D11_1.png", "Poze/D11_2.png", "Poze/D11_3.png", "Poze/D11_4.png",
         "Poze/D11_5.png", "Poze/D11_6.png", "Poze/D11_7.png", "Poze/D11_8.png"],
    48: ["Poze/D12.png", "Poze/D12_1.png", "Poze/D12_2.png", "Poze/D12_3.png", "Poze/D12_4.png",
         "Poze/D12_5.png", "Poze/D12_6.png", "Poze/D12_7.png", "Poze/D12_8.png"],

    49: ["Poze/E1.png", "Poze/E1_1.png", "Poze/E1_2.png", "Poze/E1_3.png", "Poze/E1_4.png",
         "Poze/E1_5.png", "Poze/E1_6.png", "Poze/E1_7.png", "Poze/E1_8.png"],
    50: ["Poze/E2.png", "Poze/E2_1.png", "Poze/E2_2.png", "Poze/E2_3.png", "Poze/E2_4.png",
         "Poze/E2_5.png", "Poze/E2_6.png", "Poze/E2_7.png", "Poze/E2_8.png"],
    51: ["Poze/E3.png", "Poze/E3_1.png", "Poze/E3_2.png", "Poze/E3_3.png", "Poze/E3_4.png",
         "Poze/E3_5.png", "Poze/E3_6.png", "Poze/E3_7.png", "Poze/E3_8.png"],
    52: ["Poze/E4.png", "Poze/E4_1.png", "Poze/E4_2.png", "Poze/E4_3.png", "Poze/E4_4.png",
         "Poze/E4_5.png", "Poze/E4_6.png", "Poze/E4_7.png", "Poze/E4_8.png"],
    53: ["Poze/E5.png", "Poze/E5_1.png", "Poze/E5_2.png", "Poze/E5_3.png", "Poze/E5_4.png",
         "Poze/E5_5.png", "Poze/E5_6.png", "Poze/E5_7.png", "Poze/E5_8.png"],
    54: ["Poze/E6.png", "Poze/E6_1.png", "Poze/E6_2.png", "Poze/E6_3.png", "Poze/E6_4.png",
         "Poze/E6_5.png", "Poze/E6_6.png", "Poze/E6_7.png", "Poze/E6_8.png"],
    55: ["Poze/E7.png", "Poze/E7_1.png", "Poze/E7_2.png", "Poze/E7_3.png", "Poze/E7_4.png",
         "Poze/E7_5.png", "Poze/E7_6.png", "Poze/E7_7.png", "Poze/E7_8.png"],
    56: ["Poze/E8.png", "Poze/E8_1.png", "Poze/E8_2.png", "Poze/E8_3.png", "Poze/E8_4.png",
         "Poze/E8_5.png", "Poze/E8_6.png", "Poze/E8_7.png", "Poze/E8_8.png"],
    57: ["Poze/E9.png", "Poze/E9_1.png", "Poze/E9_2.png", "Poze/E9_3.png", "Poze/E9_4.png",
         "Poze/E9_5.png", "Poze/E9_6.png", "Poze/E9_7.png", "Poze/E9_8.png"],
    58: ["Poze/E10.png", "Poze/E10_1.png", "Poze/E10_2.png", "Poze/E10_3.png", "Poze/E10_4.png",
         "Poze/E10_5.png", "Poze/E10_6.png", "Poze/E10_7.png", "Poze/E10_8.png"],
    59: ["Poze/E11.png", "Poze/E11_1.png", "Poze/E11_2.png", "Poze/E11_3.png", "Poze/E11_4.png",
         "Poze/E11_5.png", "Poze/E11_6.png", "Poze/E11_7.png", "Poze/E11_8.png"],
    60: ["Poze/E12.png", "Poze/E12_1.png", "Poze/E12_2.png", "Poze/E12_3.png", "Poze/E12_4.png",
         "Poze/E12_5.png", "Poze/E12_6.png", "Poze/E12_7.png", "Poze/E12_8.png"],
}

# explicarea testului si interpretarea rezultatelor
Explicatie = "După introducerea numelui și a vârstei, de minim 8 ani, o să fie prezentate, " \
             "pe rând, 60 de întrebări.\n\n" \
             "Primele 24 de întrebări au 6 variante de răspuns, iar restul de 36 de întrebări au 8 " \
             "variante de răspuns.\n\n" \
             "Fiecare întrebare are doar un singur rasăpuns corect, și este necesar să selectați un " \
             "răspuns înainte de a trece la următoarea întrebare.\n\n" \
             "Răspunsul este indicat ca a fiind selectat prin conturarea acestuia cu negru.\n\n" \
             "Răspunsul nu mai poate fi schimbat dupa apasarea butonului \"Continua\".\n\n" \
             "Dupa ce ați oferit un răspuns celor 60 de întrebări sau timpul de 45 minute s-a terminat " \
             "o să fie afișat rezultatu obținut."

Descriere = "    CI\t\tNivelul de inteligență\n" \
            "Peste 140\tInteligență extrem de ridicata\n" \
            "120 - 140\t\tInteligență superioară\n" \
            "110 - 119\t\tInteligență deasupra nivelului mediu\n" \
            "100 - 109\t\tInteligență de nivel mediu (bună)\n" \
            " 90 -  99\t\tInteligență de nivel mediu (slabă)\n" \
            " 80 -  89\t\tInteligență sub medie\n" \
            " 70 -  79\t\tInteligență de limită\n" \
            " 50 -  69\t\tDeficiență minimală ușoară (debilitate mintală)\n" \
            " 20 -  49\t\tDeficiență minimală (imbecilitate)\n" \
            "  0 -  19\t\tDeficiență mintală gravă (idioție)"

# initializare font si culori
myFont = ('roboto bold', 30)
bg_color = '#2d2d53'
bt_color = '#000090'
button_da_color = '#39FF14'
button_nu_color = '#f00000'
text_color = '#ffffff'


def conometru():
    global timp_final, i
    timp_actual = time.localtime()
    timp_ramas = timp_final - (timp_actual.tm_hour * 3600 + timp_actual.tm_min * 60 + timp_actual.tm_sec)
    if timp_ramas:
        timp_ramas = str(timp_ramas // 60) + " : " + str(timp_ramas % 60)
        label_timp.config(text=timp_ramas)
    else:
        i = 60
        onclick(9)

    frame2.after(1000, conometru)


# actiunile executate la apasarea butoanelor
def onclick(args):
    global i, scor, coloana_scor, rezultat, NUME, PRENUME, VARSTA, timp_final, text_rezultat
    if args == 0:
        print(nume.get(), prenume.get(), varsta.get())
        NUME = str(nume.get())
        PRENUME = str(prenume.get())
        VARSTA = int(varsta.get())
        if int(varsta.get()) == 8:
            coloana_scor = 0
        elif int(varsta.get()) == 9:
            coloana_scor = 1
        elif int(varsta.get()) == 10:
            coloana_scor = 2
        elif int(varsta.get()) == 11:
            coloana_scor = 3
        elif int(varsta.get()) == 12:
            coloana_scor = 4
        elif int(varsta.get()) == 13:
            coloana_scor = 5
        elif int(varsta.get()) == 14 or int(varsta.get()) == 15:
            coloana_scor = 6
        else:
            coloana_scor = 7

        button_continua.config(state="disabled")

        frame1.destroy()
        frame2.pack(fill=tk.BOTH, expand=True)

        timp_final = time.localtime()
        timp_final = timp_final.tm_hour * 3600 + (timp_final.tm_min + 45) * 60 + timp_final.tm_sec
        conometru()

    elif args == 1:
        button_raspuns1.config(bd=5)
        button_raspuns2.config(bd=0)
        button_raspuns3.config(bd=0)
        button_raspuns4.config(bd=0)
        button_raspuns5.config(bd=0)
        button_raspuns6.config(bd=0)
        button_raspuns7.config(bd=0)
        button_raspuns8.config(bd=0)
        button_continua.config(state="active")
        RASPUNS[(i-1) // 12][(i-1) % 12] = 1

    elif args == 2:
        button_raspuns1.config(bd=0)
        button_raspuns2.config(bd=5)
        button_raspuns3.config(bd=0)
        button_raspuns4.config(bd=0)
        button_raspuns5.config(bd=0)
        button_raspuns6.config(bd=0)
        button_raspuns7.config(bd=0)
        button_raspuns8.config(bd=0)
        button_continua.config(state="active")
        RASPUNS[(i - 1) // 12][(i - 1) % 12] = 2

    elif args == 3:
        button_raspuns1.config(bd=0)
        button_raspuns2.config(bd=0)
        button_raspuns3.config(bd=5)
        button_raspuns4.config(bd=0)
        button_raspuns5.config(bd=0)
        button_raspuns6.config(bd=0)
        button_raspuns7.config(bd=0)
        button_raspuns8.config(bd=0)
        button_continua.config(state="active")
        RASPUNS[(i - 1) // 12][(i - 1) % 12] = 3

    elif args == 4:
        button_raspuns1.config(bd=0)
        button_raspuns2.config(bd=0)
        button_raspuns3.config(bd=0)
        button_raspuns4.config(bd=5)
        button_raspuns5.config(bd=0)
        button_raspuns6.config(bd=0)
        button_raspuns7.config(bd=0)
        button_raspuns8.config(bd=0)
        button_continua.config(state="active")
        RASPUNS[(i - 1) // 12][(i - 1) % 12] = 4

    elif args == 5:
        button_raspuns1.config(bd=0)
        button_raspuns2.config(bd=0)
        button_raspuns3.config(bd=0)
        button_raspuns4.config(bd=0)
        button_raspuns5.config(bd=5)
        button_raspuns6.config(bd=0)
        button_raspuns7.config(bd=0)
        button_raspuns8.config(bd=0)
        button_continua.config(state="active")
        RASPUNS[(i - 1) // 12][(i - 1) % 12] = 5

    elif args == 6:
        button_raspuns1.config(bd=0)
        button_raspuns2.config(bd=0)
        button_raspuns3.config(bd=0)
        button_raspuns4.config(bd=0)
        button_raspuns5.config(bd=0)
        button_raspuns6.config(bd=5)
        button_raspuns7.config(bd=0)
        button_raspuns8.config(bd=0)
        button_continua.config(state="active")
        RASPUNS[(i - 1) // 12][(i - 1) % 12] = 6

    elif args == 7:
        button_raspuns1.config(bd=0)
        button_raspuns2.config(bd=0)
        button_raspuns3.config(bd=0)
        button_raspuns4.config(bd=0)
        button_raspuns5.config(bd=0)
        button_raspuns6.config(bd=0)
        button_raspuns7.config(bd=5)
        button_raspuns8.config(bd=0)
        button_continua.config(state="active")
        RASPUNS[(i - 1) // 12][(i - 1) % 12] = 7

    elif args == 8:
        button_raspuns1.config(bd=0)
        button_raspuns2.config(bd=0)
        button_raspuns3.config(bd=0)
        button_raspuns4.config(bd=0)
        button_raspuns5.config(bd=0)
        button_raspuns6.config(bd=0)
        button_raspuns7.config(bd=0)
        button_raspuns8.config(bd=5)
        button_continua.config(state="active")
        RASPUNS[(i - 1) // 12][(i - 1) % 12] = 8

    elif args == 9:
        if i == 60:
            if RASPUNS[(i - 1) // 12][(i - 1) % 12] == BAREM[(i - 1) // 12][(i - 1) % 12]:
                scor += 1

            if scor:
                rezultat = REZULTATE[scor - 1][coloana_scor]
            else:
                rezultat = 0
            if VARSTA < 35:
                ci = 100
            elif VARSTA < 40:
                ci = 97
            elif VARSTA < 45:
                ci = 93
            elif VARSTA < 50:
                ci = 83
            elif VARSTA < 55:
                ci = 82
            elif VARSTA < 60:
                ci = 76
            else:
                ci = 70

            text_rezultat = "Raspunsuri\ncorecte: " + str(scor) + "\n\nCI: " + str(rezultat * 100 // ci)
            label_raspuns.config(text=text_rezultat)

            print(RASPUNS)
            print(i)
            print(scor)

            frame2.destroy()
            frame3.pack(fill=tk.BOTH, expand=True)
        else:
            if RASPUNS[(i - 1) // 12][(i - 1) % 12] == BAREM[(i - 1) // 12][(i - 1) % 12]:
                scor += 1
            i += 1
            button_raspuns1.config(bd=0)
            button_raspuns2.config(bd=0)
            button_raspuns3.config(bd=0)
            button_raspuns4.config(bd=0)
            button_raspuns5.config(bd=0)
            button_raspuns6.config(bd=0)
            button_raspuns7.config(bd=0)
            button_raspuns8.config(bd=0)

            poza_i_n = tk.PhotoImage(file=INTREBARI[i][0])
            label_intrebare.config(image=poza_i_n)
            label_intrebare.image = poza_i_n
            poza_r1_n = tk.PhotoImage(file=INTREBARI[i][1])
            button_raspuns1.config(image=poza_r1_n)
            button_raspuns1.image = poza_r1_n
            poza_r2_n = tk.PhotoImage(file=INTREBARI[i][2])
            button_raspuns2.config(image=poza_r2_n)
            button_raspuns2.image = poza_r2_n
            poza_r3_n = tk.PhotoImage(file=INTREBARI[i][3])
            button_raspuns3.config(image=poza_r3_n)
            button_raspuns3.image = poza_r3_n
            poza_r4_n = tk.PhotoImage(file=INTREBARI[i][4])
            button_raspuns4.config(image=poza_r4_n)
            button_raspuns4.image = poza_r4_n
            poza_r5_n = tk.PhotoImage(file=INTREBARI[i][5])
            button_raspuns5.config(image=poza_r5_n)
            button_raspuns5.image = poza_r5_n
            poza_r6_n = tk.PhotoImage(file=INTREBARI[i][6])
            button_raspuns6.config(image=poza_r6_n)
            button_raspuns6.image = poza_r6_n

            if i > 24:
                poza_r7_n = tk.PhotoImage(file=INTREBARI[i][7])
                button_raspuns7.config(image=poza_r7_n)
                button_raspuns7.image = poza_r7_n
                poza_r8_n = tk.PhotoImage(file=INTREBARI[i][8])
                button_raspuns8.config(image=poza_r8_n)
                button_raspuns8.image = poza_r8_n

            button_continua.config(state="disabled")

    # args == 10 salveaza rezultatul in fisie
    # daca fisierul exista, atunci updateaza continutul
    # altfel il creaza
    elif args == 10:
        titlu = "Rezultat test RAVEN " + NUME + " " + PRENUME + ".txt"
        file_raspuns = open(titlu, 'w+')
        file_raspuns.write(text_rezultat)
        file_raspuns.close()
        os.startfile(titlu)

    # args == 11 inchide testul
    elif args == 11:
        exit()

    # args == 12 explicarea testului si inceperea lui
    elif args == 12:
        frame0.destroy()
        frame1.pack(fill=tk.BOTH, expand=True)


window = tk.Tk()
window.state('zoomed')
window.title("Test RAVEN")


# frame 0
frame0 = tk.Frame(window, bg=bg_color)
frame0.grid_rowconfigure(0, weight=1)
frame0.grid_rowconfigure(1, weight=0)
frame0.grid_columnconfigure(0, weight=1)
frame0.grid_columnconfigure(1, weight=0)

label_explicatie = tk.Label(frame0, text=Explicatie, font=myFont, justify=tk.LEFT, fg="white", bg=bg_color, wrap=1300)
button_start = tk.Button(frame0, text="Începe", font=myFont, bg=bt_color, fg="white", command=lambda: onclick(12))

frame0.pack(fill=tk.BOTH, expand=True)
label_explicatie.grid(row=0, column=0)
button_start.grid(row=1, column=1)

# frame1 - introducerea numelui si a varstei
frame1 = tk.Frame(window, bg=bg_color)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_rowconfigure(4, weight=1)
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(4, weight=1)

label_nume = tk.Label(frame1, text="Numele: ", font=myFont, justify=tk.LEFT, fg="white", bg=bg_color)
nume = tk.Entry(frame1, font=myFont)
label_prenume = tk.Label(frame1, text="Prenumele: ", font=myFont, justify=tk.LEFT, fg="white", bg=bg_color)
prenume = tk.Entry(frame1, font=myFont)
label_varsta = tk.Label(frame1, text="Vârsta: ", font=myFont, justify=tk.LEFT, fg="white", bg=bg_color)
varsta = tk.Entry(frame1, font=myFont)

button_continua = tk.Button(frame1, text="Continua", font=myFont, bg=bt_color, fg="white", command=lambda: onclick(0))


label_nume.grid(row=1, column=1, sticky=tk.E)
nume.grid(row=1, column=2, sticky=tk.W)
label_prenume.grid(row=2, column=1, sticky=tk.E)
prenume.grid(row=2, column=2, sticky=tk.W)
label_varsta.grid(row=3, column=1, sticky=tk.E)
varsta.grid(row=3, column=2, sticky=tk.W)
button_continua.grid(row=4, column=2, sticky=tk.NE)


# in frame2 sunt afisate intrebarile si se dau raspunsurile
frame2 = tk.Frame(window)

poza_i = tk.PhotoImage(file=INTREBARI[i][0])
label_intrebare = tk.Label(frame2, image=poza_i, bg='#fdfdfd')
label_timp = tk.Label(frame2, bg='#fdfdfd', font=myFont)
poza_r1 = tk.PhotoImage(file=INTREBARI[i][1])
button_raspuns1 = tk.Button(frame2, image=poza_r1, bg='#fdfdfd', bd=0, command=lambda: onclick(1))
poza_r2 = tk.PhotoImage(file=INTREBARI[i][2])
button_raspuns2 = tk.Button(frame2, image=poza_r2, bg='#fdfdfd', bd=0, command=lambda: onclick(2))
poza_r3 = tk.PhotoImage(file=INTREBARI[i][3])
button_raspuns3 = tk.Button(frame2, image=poza_r3, bg='#fdfdfd', bd=0, command=lambda: onclick(3))
poza_r4 = tk.PhotoImage(file=INTREBARI[i][4])
button_raspuns4 = tk.Button(frame2, image=poza_r4, bg='#fdfdfd', bd=0, command=lambda: onclick(4))
poza_r5 = tk.PhotoImage(file=INTREBARI[i][5])
button_raspuns5 = tk.Button(frame2, image=poza_r5, bg='#fdfdfd', bd=0, command=lambda: onclick(5))
poza_r6 = tk.PhotoImage(file=INTREBARI[i][6])
button_raspuns6 = tk.Button(frame2, image=poza_r6, bg='#fdfdfd', bd=0, command=lambda: onclick(6))
button_raspuns7 = tk.Button(frame2, bg='#fdfdfd', bd=0, command=lambda: onclick(7))
button_raspuns8 = tk.Button(frame2, bg='#fdfdfd', bd=0, command=lambda: onclick(8))

button_continua = tk.Button(frame2, text="Continua", font=myFont, bg=bt_color, fg="white", command=lambda: onclick(9))


label_timp.grid(row=0, column=0, sticky=tk.E)
label_intrebare.grid(row=1, column=0, rowspan=3)
button_raspuns1.grid(row=0, column=1, sticky=tk.E)
button_raspuns2.grid(row=0, column=2, sticky=tk.W)
button_raspuns3.grid(row=1, column=1, sticky=tk.E)
button_raspuns4.grid(row=1, column=2, sticky=tk.W)
button_raspuns5.grid(row=2, column=1, sticky=tk.E)
button_raspuns6.grid(row=2, column=2, sticky=tk.W)
button_raspuns7.grid(row=3, column=1, sticky=tk.W)
button_raspuns8.grid(row=3, column=2, sticky=tk.W)

button_continua.grid(row=4, column=2, sticky=tk.NE)


# in frame3 se afiseza rezultatul si interpretarea testului si de aizi se poate salva rezultatul in fisier
frame3 = tk.Frame(window, bg=bg_color)
frame3a = tk.Frame(frame3)

rezultat = REZULTATE[scor][coloana_scor]
label_raspuns = tk.Label(frame3a, text="Rezultat test: " + str(rezultat), font=myFont,
                         justify=tk.LEFT, fg=text_color, bg=bg_color)
button_safe = tk.Button(frame3a, text="Salveaza\nRezultat", font=myFont, bg=bg_color, bd=0,
                        fg=text_color, command=lambda: onclick(10))
button_exit = tk.Button(frame3a, text="Inchide\nTesul", font=myFont, bg=bg_color, bd=0,
                        fg=text_color, command=lambda: onclick(11))
label_raspuns.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
button_safe.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
button_exit.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3b = tk.Frame(frame3)
text_descriere = tk.Label(frame3b, text=Descriere, font=myFont, fg=text_color, bg=bg_color, justify=tk.LEFT)
text_descriere.pack(fill=tk.BOTH, expand=True)

frame3a.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame3b.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)


window.mainloop()
