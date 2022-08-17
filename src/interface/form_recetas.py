from distutils.cmd import Command
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
import utils.generic as utl
import components.components as cmp
import time
from model.proceso import DBProceso


class RecetasMenu:

    def getElement(self, event):
        selection = event.widget.curselection()
        index = selection[0]
        self.value = event.widget.get(index)
        # result.set(value)
        print(index, ' -> ', self.value)
        self.labels_entry()
        
    def labels_entry(self):
        print("VAKUES")
        print(self.value)
        print()

        ren = self.con.select_proceso(self.value)
       
        # print(DBProceso.select_proceso)

        self.valor16 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor16.insert(0, ren[0])
        self.valor16.grid(row=1, column=2, padx=100)

        self.valor17 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor17.insert(0, ren[1])
        self.valor17.grid(row=2, column=2, padx=100)

        self.valor18 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor18.insert(0, ren[2])
        self.valor18.grid(row=3, column=2, padx=100)

        self.valor19 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor19.insert(0, ren[3])
        self.valor19.grid(row=4, column=2, padx=100)

        self.valor20 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor20.insert(0, ren[4])
        self.valor20.grid(row=5, column=2, padx=100)

        self.valor21 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor21.insert(0, ren[5])
        self.valor21.grid(row=6, column=2, padx=100)

        self.valor22 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor22.insert(0, ren[6])
        self.valor22.grid(row=7, column=2, padx=100)

        self.valor23 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor23.insert(0, ren[7])
        self.valor23.grid(row=8, column=2, padx=100)

        self.valor25 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor25.insert(0, ren[8])
        self.valor25.grid(row=10, column=2, padx=100)

        self.valor26 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor26.insert(0, ren[9])
        self.valor26.grid(row=11, column=2, padx=100)

        self.valor27 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor27.insert(0, ren[10])
        self.valor27.grid(row=12, column=2, padx=100)

        self.valor29 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor29.insert(0, ren[11])
        self.valor29.grid(row=14, column=2, padx=100)

        self.valor30 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor30.insert(0, ren[12])
        self.valor30.grid(row=15, column=2, padx=100)

        self.valor31 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor31.insert(0, ren[13])
        self.valor31.grid(row=16, column=2, padx=100)

        self.valor32 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor32.insert(0, ren[14])
        self.valor32.grid(row=17, column=2, padx=100)

        self.valor33 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor33.insert(0, ren[15])
        self.valor33.grid(row=18, column=2, padx=100)

        self.valor34 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor34.insert(0, ren[16])
        self.valor34.grid(row=19, column=2, padx=100)

        self.valor35 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor35.insert(0, ren[17])
        self.valor35.grid(row=20, column=2, padx=100)

        self.valor36 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor36.insert(0, ren[18])
        self.valor36.grid(row=21, column=2, padx=100)

        self.valor37 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor37.insert(0, ren[19])
        self.valor37.grid(row=22, column=2, padx=100)

        self.valor38 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor38.insert(0, ren[20])
        self.valor38.grid(row=23, column=2, padx=100)

        self.valor39 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor39.insert(0, ren[21])
        self.valor39.grid(row=24, column=2, padx=100)

        self.valor40 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor40.insert(0, '0')
        self.valor40.grid(row=25, column=2, padx=100)

        self.valor41 = tk.Entry(
            self.second_frame, width=20, bg="#ff8fff", fg="#000000")
        self.valor41.insert(0, ren[23])
        self.valor41.grid(row=26, column=2, padx=100)

        self.valor47 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor47.insert(0, ren[24])
        self.valor47.grid(row=28, column=2, padx=100)

        self.valor48 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor48.insert(0, ren[25])
        self.valor48.grid(row=29, column=2, padx=100)

        self.valor49 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor49.insert(0, ren[26])
        self.valor49.grid(row=30, column=2, padx=100)

        self.valor50 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor50.insert(0, ren[27])
        self.valor50.grid(row=31, column=2, padx=100)

        self.valor51 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor51.insert(0, ren[28])
        self.valor51.grid(row=32, column=2, padx=100)

        self.valor52 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor52.insert(0, ren[29])
        self.valor52.grid(row=33, column=2, padx=100)

        self.valor53 = tk.Entry(
            self.second_frame, width=20, bg="#3fffff", fg="#000000")
        self.valor53.insert(0, ren[30])
        self.valor53.grid(row=34, column=2, padx=100)

        self.valor71 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor71.insert(0, ren[31])
        self.valor71.grid(row=36, column=2, padx=100)

        self.valor72 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor72.insert(0, ren[32])
        self.valor72.grid(row=37, column=2, padx=100)

        self.valor73 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor73.insert(0, ren[33])
        self.valor73.grid(row=38, column=2, padx=100)

        self.valor74 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor74.insert(0, ren[34])
        self.valor74.grid(row=39, column=2, padx=100)

        self.valor75 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor75.insert(0,  ren[35])
        self.valor75.grid(row=40, column=2, padx=100)

        self.valor76 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor76.insert(0, ren[36])
        self.valor76.grid(row=41, column=2, padx=100)

        self.valor77 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor77.insert(0, ren[37])
        self.valor77.grid(row=42, column=2, padx=100)

        self.valor78 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor78.insert(0, ren[38])
        self.valor78.grid(row=43, column=2, padx=100)

        self.valor87 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor87.insert(0, ren[39])
        self.valor87.grid(row=45, column=2, padx=100)

        self.valor88 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor88.insert(0, ren[40])
        self.valor88.grid(row=46, column=2, padx=100)

        self.valor89 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor89.insert(0, ren[41])
        self.valor89.grid(row=47, column=2, padx=100)

        self.valor90 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor90.insert(0,  ren[42])
        self.valor90.grid(row=48, column=2, padx=100)

        self.valor91 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor91.insert(0, ren[43])
        self.valor91.grid(row=49, column=2, padx=100)

        self.valor92 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor92.insert(0, ren[44])
        self.valor92.grid(row=50, column=2, padx=100)

        self.valor94 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor94.insert(0, ren[45])
        self.valor94.grid(row=52, column=2, padx=100)

        self.valor95 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor95.insert(0, ren[46])
        self.valor95.grid(row=53, column=2, padx=100)

        self.valor96 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor96.insert(0, ren[47])
        self.valor96.grid(row=54, column=2, padx=100)

        self.valor97 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor97.insert(0, ren[48])
        self.valor97.grid(row=55, column=2, padx=100)

        self.valor98 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor98.insert(0, ren[49])
        self.valor98.grid(row=56, column=2, padx=100)

        self.valor99 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor99.insert(0, ren[50])
        self.valor99.grid(row=57, column=2, padx=100)

        self.valor100 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor100.insert(0, ren[51])
        self.valor100.grid(row=58, column=2, padx=100)

        self.valor101 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor101.insert(0, ren[52])
        self.valor101.grid(row=59, column=2, padx=100)

        self.valor102 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor102.insert(0, ren[53])
        self.valor102.grid(row=60, column=2, padx=100)

        self.valor103 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor103.insert(0, ren[54])
        self.valor103.grid(row=61, column=2, padx=100)

        self.valor104 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor104.insert(0, ren[55])
        self.valor104.grid(row=62, column=2, padx=100)

        self.valor107 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor107.insert(0, ren[56])
        self.valor107.grid(row=64, column=2, padx=100)

        self.valor108 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor108.insert(0, ren[57])
        self.valor108.grid(row=65, column=2, padx=100)

        self.valor109 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor109.insert(0, ren[58])
        self.valor109.grid(row=66, column=2, padx=100)

        self.valor110 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor110.insert(0, ren[59])
        self.valor110.grid(row=67, column=2, padx=100)

        self.valor111 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor111.insert(0, ren[60])
        self.valor111.grid(row=68, column=2, padx=100)

        self.valor112 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor112.insert(0, ren[61])
        self.valor112.grid(row=69, column=2, padx=100)

        self.valor113 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor113.insert(0, ren[62])
        self.valor113.grid(row=70, column=2, padx=100)

        self.valor114 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor114.insert(0, ren[63])
        self.valor114.grid(row=71, column=2, padx=100)

        self.valor115 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor115.insert(0, ren[64])
        self.valor115.grid(row=72, column=2, padx=100)

        self.valor117 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor117.insert(0, ren[65])
        self.valor117.grid(row=75, column=2, padx=100)

        self.valor118 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor118.insert(0, ren[66])
        self.valor118.grid(row=76, column=2, padx=100)

        self.valor119 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor119.insert(0, ren[67])
        self.valor119.grid(row=77, column=2, padx=100)

        self.valor120 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor120.insert(0, ren[68])
        self.valor120.grid(row=78, column=2, padx=100)

        self.valor121 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor121.insert(0, ren[69])
        self.valor121.grid(row=79, column=2, padx=100)

        self.valor122 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor122.insert(0, ren[70])
        self.valor122.grid(row=80, column=2, padx=100)

        self.valor123 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor123.insert(0, ren[71])
        self.valor123.grid(row=81, column=2, padx=100)

        self.valor124 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor124.insert(0, ren[72])
        self.valor124.grid(row=82, column=2, padx=100)

        self.valor125 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor125.insert(0, ren[73])
        self.valor125.grid(row=83, column=2, padx=100)

        self.valor126 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor126.insert(0, ren[74])
        self.valor126.grid(row=84, column=2, padx=100)

        self.valor127 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor127.insert(0, ren[75])
        self.valor127.grid(row=85, column=2, padx=100)

        self.valor128 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor128.insert(0, ren[76])
        self.valor128.grid(row=86, column=2, padx=100)

        self.valor129 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor129.insert(0, ren[77])
        self.valor129.grid(row=87, column=2, padx=100)

        self.valor130 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor130.insert(0, ren[78])
        self.valor130.grid(row=88, column=2, padx=100)

        self.valor131 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor131.insert(0, ren[79])
        self.valor131.grid(row=89, column=2, padx=100)

        self.valor132 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor132.insert(0, ren[80])
        self.valor132.grid(row=90, column=2, padx=100)

        self.valor133 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor133.insert(0, ren[81])
        self.valor133.grid(row=91, column=2, padx=100)

        self.valor134 = tk.Entry(
            self.second_frame, width=20, bg="#ff5fff", fg="#000000")
        self.valor134.insert(0, ren[82])
        self.valor134.grid(row=94, column=2, padx=100)

        self.valor135 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor135.insert(0, ren[83])
        self.valor135.grid(row=95, column=2, padx=100)

        self.valor136 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor136.insert(0, ren[84])
        self.valor136.grid(row=96, column=2, padx=100)

        self.valor137 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor137.insert(0, ren[85])
        self.valor137.grid(row=97, column=2, padx=100)

        self.valor138 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor138.insert(0, ren[86])
        self.valor138.grid(row=98, column=2, padx=100)

        self.valor139 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor139.insert(0, ren[87])
        self.valor139.grid(row=99, column=2, padx=100)

        self.valor140 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor140.insert(0, ren[88])
        self.valor140.grid(row=100, column=2, padx=100)

        self.valor141 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor141.insert(0, ren[89])
        self.valor141.grid(row=101, column=2, padx=100)

        self.valor142 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor142.insert(0, ren[90])
        self.valor142.grid(row=102, column=2, padx=100)

        self.valor143 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor143.insert(0, ren[91])
        self.valor143.grid(row=103, column=2, padx=100)

        self.valor144 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor144.insert(0, ren[92])
        self.valor144.grid(row=104, column=2, padx=100)

        self.valor145 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor145.insert(0, ren[93])
        self.valor145.grid(row=105, column=2, padx=100)

        self.valor146 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor146.insert(0, ren[94])
        self.valor146.grid(row=106, column=2, padx=100)

        self.valor147 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor147.insert(0, ren[95])
        self.valor147.grid(row=107, column=2, padx=100)

        self.valor148 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor148.insert(0, ren[96])
        self.valor148.grid(row=108, column=2, padx=100)

        self.valor149 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor149.insert(0, ren[97])
        self.valor149.grid(row=109, column=2, padx=100)

        self.valor150 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor150.insert(0, ren[98])
        self.valor150.grid(row=110, column=2, padx=100)

        self.valor169 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor169.insert(0, ren[99])
        self.valor169.grid(row=112, column=2, padx=100)

        self.valor170 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor170.insert(0, ren[100])
        self.valor170.grid(row=113, column=2, padx=100)

        self.valor171 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor171.insert(0, ren[101])
        self.valor171.grid(row=114, column=2, padx=100)

        self.valor172 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor172.insert(0, ren[102])
        self.valor172.grid(row=115, column=2, padx=100)

        self.valor173 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor173.insert(0, ren[103])
        self.valor173.grid(row=116, column=2, padx=100)

        self.valor174 = tk.Entry(
            self.second_frame, width=20, bg="#ffffff", fg="#000000")
        self.valor174.insert(0, ren[104])
        self.valor174.grid(row=117, column=2, padx=100)

    def disable_edit(self):
        # entry = ttk.Entry(state=tk.DISABLED)
        self.valor16.config(state="readonly")
        self.valor17.config(state="readonly")
        self.valor18.config(state="readonly")
        self.valor19.config(state="readonly")
        self.valor20.config(state="readonly")
        self.valor21.config(state="readonly")
        self.valor22.config(state="readonly")
        self.valor23.config(state="readonly")
        self.valor25.config(state="readonly")
        self.valor26.config(state="readonly")
        self.valor27.config(state="readonly")
        self.valor29.config(state="readonly")
        self.valor30.config(state="readonly")
        self.valor31.config(state="readonly")
        self.valor32.config(state="readonly")
        self.valor33.config(state="readonly")
        self.valor34.config(state="readonly")
        self.valor35.config(state="readonly")
        self.valor36.config(state="readonly")
        self.valor37.config(state="readonly")
        self.valor38.config(state="readonly")
        self.valor39.config(state="readonly")
        self.valor40.config(state="readonly")
        self.valor41.config(state="readonly")
        self.valor47.config(state="readonly")
        self.valor48.config(state="readonly")
        self.valor49.config(state="readonly")
        self.valor50.config(state="readonly")
        self.valor51.config(state="readonly")
        self.valor52.config(state="readonly")
        self.valor53.config(state="readonly")
        self.valor71.config(state="readonly")
        self.valor72.config(state="readonly")
        self.valor73.config(state="readonly")
        self.valor74.config(state="readonly")
        self.valor75.config(state="readonly")
        self.valor76.config(state="readonly")
        self.valor77.config(state="readonly")
        self.valor78.config(state="readonly")
        self.valor87.config(state="readonly")
        self.valor88.config(state="readonly")
        self.valor89.config(state="readonly")
        self.valor90.config(state="readonly")
        self.valor91.config(state="readonly")
        self.valor92.config(state="readonly")
        self.valor94.config(state="readonly")
        self.valor95.config(state="readonly")
        self.valor96.config(state="readonly")
        self.valor97.config(state="readonly")
        self.valor98.config(state="readonly")
        self.valor99.config(state="readonly")
        self.valor100.config(state="readonly")
        self.valor101.config(state="readonly")
        self.valor102.config(state="readonly")
        self.valor103.config(state="readonly")
        self.valor104.config(state="readonly")
        self.valor107.config(state="readonly")
        self.valor108.config(state="readonly")
        self.valor109.config(state="readonly")
        self.valor110.config(state="readonly")
        self.valor111.config(state="readonly")
        self.valor112.config(state="readonly")
        self.valor113.config(state="readonly")
        self.valor114.config(state="readonly")
        self.valor115.config(state="readonly")
        self.valor117.config(state="readonly")
        self.valor118.config(state="readonly")
        self.valor119.config(state="readonly")
        self.valor120.config(state="readonly")
        self.valor121.config(state="readonly")
        self.valor122.config(state="readonly")
        self.valor123.config(state="readonly")
        self.valor124.config(state="readonly")
        self.valor125.config(state="readonly")
        self.valor126.config(state="readonly")
        self.valor127.config(state="readonly")
        self.valor128.config(state="readonly")
        self.valor129.config(state="readonly")
        self.valor130.config(state="readonly")
        self.valor131.config(state="readonly")
        self.valor132.config(state="readonly")
        self.valor133.config(state="readonly")
        self.valor134.config(state="readonly")
        self.valor135.config(state="readonly")
        self.valor136.config(state="readonly")
        self.valor137.config(state="readonly")
        self.valor138.config(state="readonly")
        self.valor139.config(state="readonly")
        self.valor140.config(state="readonly")
        self.valor141.config(state="readonly")
        self.valor142.config(state="readonly")
        self.valor143.config(state="readonly")
        self.valor144.config(state="readonly")
        self.valor145.config(state="readonly")
        self.valor146.config(state="readonly")
        self.valor147.config(state="readonly")
        self.valor148.config(state="readonly")
        self.valor149.config(state="readonly")
        self.valor150.config(state="readonly")
        self.valor169.config(state="readonly")
        self.valor170.config(state="readonly")
        self.valor171.config(state="readonly")
        self.valor172.config(state="readonly")
        self.valor173.config(state="readonly")
        self.valor174.config(state="readonly")

    def enable_edit(self):
        # entry = ttk.Entry(state="readonly")
        self.valor16.config(state=tk.NORMAL)
        self.valor17.config(state=tk.NORMAL)
        self.valor18.config(state=tk.NORMAL)
        self.valor19.config(state=tk.NORMAL)
        self.valor20.config(state=tk.NORMAL)
        self.valor21.config(state=tk.NORMAL)
        self.valor22.config(state=tk.NORMAL)
        self.valor23.config(state=tk.NORMAL)
        self.valor25.config(state=tk.NORMAL)
        self.valor26.config(state=tk.NORMAL)
        self.valor27.config(state=tk.NORMAL)
        self.valor29.config(state=tk.NORMAL)
        self.valor30.config(state=tk.NORMAL)
        self.valor31.config(state=tk.NORMAL)
        self.valor32.config(state=tk.NORMAL)
        self.valor33.config(state=tk.NORMAL)
        self.valor34.config(state=tk.NORMAL)
        self.valor35.config(state=tk.NORMAL)
        self.valor36.config(state=tk.NORMAL)
        self.valor37.config(state=tk.NORMAL)
        self.valor38.config(state=tk.NORMAL)
        self.valor39.config(state=tk.NORMAL)
        self.valor40.config(state=tk.NORMAL)
        self.valor41.config(state=tk.NORMAL)
        self.valor47.config(state=tk.NORMAL)
        self.valor48.config(state=tk.NORMAL)
        self.valor49.config(state=tk.NORMAL)
        self.valor50.config(state=tk.NORMAL)
        self.valor51.config(state=tk.NORMAL)
        self.valor52.config(state=tk.NORMAL)
        self.valor53.config(state=tk.NORMAL)
        self.valor71.config(state=tk.NORMAL)
        self.valor72.config(state=tk.NORMAL)
        self.valor73.config(state=tk.NORMAL)
        self.valor74.config(state=tk.NORMAL)
        self.valor75.config(state=tk.NORMAL)
        self.valor76.config(state=tk.NORMAL)
        self.valor77.config(state=tk.NORMAL)
        self.valor78.config(state=tk.NORMAL)
        self.valor87.config(state=tk.NORMAL)
        self.valor88.config(state=tk.NORMAL)
        self.valor89.config(state=tk.NORMAL)
        self.valor90.config(state=tk.NORMAL)
        self.valor91.config(state=tk.NORMAL)
        self.valor92.config(state=tk.NORMAL)
        self.valor94.config(state=tk.NORMAL)
        self.valor95.config(state=tk.NORMAL)
        self.valor96.config(state=tk.NORMAL)
        self.valor97.config(state=tk.NORMAL)
        self.valor98.config(state=tk.NORMAL)
        self.valor99.config(state=tk.NORMAL)
        self.valor100.config(state=tk.NORMAL)
        self.valor101.config(state=tk.NORMAL)
        self.valor102.config(state=tk.NORMAL)
        self.valor103.config(state=tk.NORMAL)
        self.valor104.config(state=tk.NORMAL)
        self.valor107.config(state=tk.NORMAL)
        self.valor108.config(state=tk.NORMAL)
        self.valor109.config(state=tk.NORMAL)
        self.valor110.config(state=tk.NORMAL)
        self.valor111.config(state=tk.NORMAL)
        self.valor112.config(state=tk.NORMAL)
        self.valor113.config(state=tk.NORMAL)
        self.valor114.config(state=tk.NORMAL)
        self.valor115.config(state=tk.NORMAL)
        self.valor117.config(state=tk.NORMAL)
        self.valor118.config(state=tk.NORMAL)
        self.valor119.config(state=tk.NORMAL)
        self.valor120.config(state=tk.NORMAL)
        self.valor121.config(state=tk.NORMAL)
        self.valor122.config(state=tk.NORMAL)
        self.valor123.config(state=tk.NORMAL)
        self.valor124.config(state=tk.NORMAL)
        self.valor125.config(state=tk.NORMAL)
        self.valor126.config(state=tk.NORMAL)
        self.valor127.config(state=tk.NORMAL)
        self.valor128.config(state=tk.NORMAL)
        self.valor129.config(state=tk.NORMAL)
        self.valor130.config(state=tk.NORMAL)
        self.valor131.config(state=tk.NORMAL)
        self.valor132.config(state=tk.NORMAL)
        self.valor133.config(state=tk.NORMAL)
        self.valor134.config(state=tk.NORMAL)
        self.valor135.config(state=tk.NORMAL)
        self.valor136.config(state=tk.NORMAL)
        self.valor137.config(state=tk.NORMAL)
        self.valor138.config(state=tk.NORMAL)
        self.valor139.config(state=tk.NORMAL)
        self.valor140.config(state=tk.NORMAL)
        self.valor141.config(state=tk.NORMAL)
        self.valor142.config(state=tk.NORMAL)
        self.valor143.config(state=tk.NORMAL)
        self.valor144.config(state=tk.NORMAL)
        self.valor145.config(state=tk.NORMAL)
        self.valor146.config(state=tk.NORMAL)
        self.valor147.config(state=tk.NORMAL)
        self.valor148.config(state=tk.NORMAL)
        self.valor149.config(state=tk.NORMAL)
        self.valor150.config(state=tk.NORMAL)
        self.valor169.config(state=tk.NORMAL)
        self.valor170.config(state=tk.NORMAL)
        self.valor171.config(state=tk.NORMAL)
        self.valor172.config(state=tk.NORMAL)
        self.valor173.config(state=tk.NORMAL)
        self.valor174.config(state=tk.NORMAL)

    def LabelsUnits(self, nombres, inicio):
        j = inicio
        for i in range(len(nombres)):
            tk.Label(self.second_frame, text=nombres[i], font=('Times', 15, BOLD), bg="#ffffff",
                     fg="#000000").grid(row=int(j), column=2, sticky=tk.E)
            j = j + 1
            
    def Labels(self, nombres, inicio, numeracion):
        j = inicio
        n = numeracion

        for i in range(len(nombres)):
            #print("entro ")
            tk.Label(self.second_frame, text=str(n), font=('Times', 15, BOLD), bg="#ffffff", fg="#000000").grid(row=int(j),
                                                                                                                column=0, sticky=tk.W)
            tk.Label(self.second_frame, text=nombres[i], font=('Times', 15, BOLD), bg="#ffffff", fg="#000000").grid(row=int(j),
                                                                                                                    column=1, sticky=tk.W, pady=5, padx=10)
            j = j + 1
            n = n + 1
            print(j)

    def times(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text=current_time)
        self.date.config(text=time.strftime("%d/%m/%Y"))
        self.clock.after(200, self.times)

    def __init__(self):
        root = Tk()
        root.title("Pre Calentamiento")
        root.geometry("1200x800")
        self.con = DBProceso()
        self.value = "Receta01"

        # header
        # ------------------------------------------------------
        frame_form_top = tk.Frame(
            root, height=50, bd=0, padx=10, relief=tk.SOLID, bg="#ffffff")
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Sterilization System", font=(
            'Times', 30), bg="#ffffff", fg="#000000", pady=0)
        title.pack(side="left")

        self.date = tk.Label(frame_form_top, font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#666a88", padx=25)
        self.date.pack(side="right")

        self.clock = tk.Label(frame_form_top, font=(
            'Times', 15, BOLD), bg="#ffffff", fg="black", padx=25, pady=20)
        self.clock.pack(side="right")
        self.times()

        text_temperatura = tk.Label(frame_form_top, text="Temperatura: ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text_temperatura.pack(side="left", padx=80)

        temperatura = tk.Label(frame_form_top, text="20°C", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000", padx=0)
        temperatura.pack(side="left")
        # TERMINA HEADER
        # ----------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------

        # FRAME PARA LISTA Y BOTONES DE RECETAS
        frame_left = tk.Frame(root, bd=0, relief=tk.SOLID,
                              width=40, padx=10, pady=10, bg="#ffffff")
        frame_left.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        lista = tk.Listbox(frame_left, height=10, bd=0, relief=tk.SOLID,
                           bg="#fcfcfc", fg="#666a88", font=('Times', 15, BOLD))
        lista.pack(side="top", expand=tk.NO, fill=tk.X)
        lista.bind('<<ListboxSelect>>', self.getElement)

        names = self.con.select_all_name_proceso()
        print("names: ")
        print(names)

        for i in range(len(names)):
            lista.insert(0, names[i])

        boton_crear = tk.Button(frame_left, text="Crear", font=(
            'Times', 15, BOLD), bg="green", bd=0, fg="#fff")
        boton_crear.pack(side="top", expand=tk.NO, fill=tk.X, pady=5)

        boton_editar = tk.Button(frame_left, text="Editar", font=(
            'Times', 15, BOLD), bg="yellow", bd=0, fg="#fff", command=self.enable_edit)
        boton_editar.pack(side="top", expand=tk.NO, fill=tk.X, pady=5)

        boton_eliminar = tk.Button(frame_left, text="Eliminar", font=(
            'Times', 15, BOLD), bg="red", bd=0, fg="#fff")
        boton_eliminar.pack(side="top", expand=tk.NO, fill=tk.X, pady=10)

        boton_eliminar = tk.Button(frame_left, text="Guardar", font=(
            'Times', 15, BOLD), bg="blue", bd=0, fg="#fff", state=tk.DISABLED)
        boton_eliminar.pack(side="bottom", expand=tk.NO, fill=tk.X, pady=5)

        boton_eliminar = tk.Button(frame_left, text="Cancelar", font=(
            'Times', 15, BOLD), bg="orange", bd=0, fg="#fff", state=tk.DISABLED)
        boton_eliminar.pack(side="bottom", expand=tk.NO, fill=tk.X, pady=5, )

        # main frame
        main_frame = Frame(root, bg="#ffffff")
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        # canvas
        canvas = Canvas(main_frame, bg="#ffffff")
        canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        # scroll bar to canvas
        scroll_bar = Scrollbar(main_frame, orient=VERTICAL,
                               command=canvas.yview, bg="#ffffff")
        scroll_bar.pack(side=RIGHT, fill=Y)
        # configure the canvas
        canvas.configure(yscrollcommand=scroll_bar.set)

        canvas.bind('<Configure>', lambda e: canvas.configure(
            scrollregion=canvas.bbox('all')))
        # create another frame inside the canvas
        self.second_frame = Frame(canvas, bg="#ffffff")
        self.second_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # add thet new frame to a window in the canvas
        canvas.create_window((0, 0), window=self.second_frame, anchor='nw')

        # for thing in range(100):
        #    Button(self.second_frame, text=thing, width=10).grid(row=thing, column=0)

        # labe = Label(self.second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
        #labe.grid(row=3, column=2)
        # labe2 = Label(self.second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
        #labe2.grid(row=3, column=3)
        self.second_frame.columnconfigure(0, weight=1)
        self.second_frame.rowconfigure(200, weight=15)

        text11 = tk.Label(self.second_frame, text="VACUUM", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text11.grid(row=0, column=2, sticky=tk.W)
        # text12 = tk.Label(self.second_frame, text = "1", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        #text12.grid(row = 1, column = 0, sticky = tk.W)
        self.Labels(["Evacuation Pressure: ", "Anti-cavitation Pressure: ", "Gas Interlock Pressure: ", "Pressure Increment: ",
                     "Time Increment: ", "Fast Increment Tolerance: ", "Slow Increment Termination Pressure: ", "Print Interval: "], 1, 16)

        # text12 = tk.Label(self.second_frame, text = "F", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        #text12.grid(row = 1, column = 2, sticky = tk.E)
        self.LabelsUnits(["INHGA", "INHGA", "INHGA", "INHG",
                         "MM:SS", "INHG", "INHGA", "MM:SS"], 1)

        text9 = tk.Label(self.second_frame, text="LEAK TEST ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text9.grid(row=9, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Leak Test Time", "Leak Test Tolerance",
                    "Print Interval"], 10, 25)
        self.LabelsUnits(["HH:MM", "INHG", "MM:SS"], 10)

        text13 = tk.Label(self.second_frame, text="INERT DILUTION", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text13.grid(row=13, column=2, pady=5, padx=10)

        self.Labels(["# Of Dilution Cycles", "Inert Gas Pressure", "Inert Pressure Increment", "Inert Time Increment", "Inert Fast Increment Tolerance",
                     "Evacuation Pressure", "Vacuum Pressure Increment", "Vacuum Time Increment", "Vacuum Fast Inc Tolerance", "Vacuum Slow Inc Termination Pressure",
                     "Anti-cavitation pressure", "Hi Pressure", "Print Interval"], 14, 29)
        self.LabelsUnits(["", "INHGA", "INHG", "MM:SS", "INHG", "INHGA",
                         "INHG", "MM:SS", "INHG", "INHGA", "INHGA", "INHGA", "MM:SS"], 14)

        text9 = tk.Label(self.second_frame, text="HUMIDIFICATION ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text9.grid(row=27, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Type", "Pressure Rise", "Pressure Increment", "Time Increment", "Fast Increment Tolerance",
                     "Maximum Time", "Print Interval"],  28, 47)
        self.LabelsUnits(["", "INHG", "INHG", "MM:SS",
                         "INHG", "HH:MM", "MM:SS"], 28)

        text27 = tk.Label(self.second_frame, text="HUMIDITY DWELL ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text27.grid(row=35, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Type", "Control Pressure", "Control Differential", "Hi Humidity",
                    "Lo Humidity", "Maximum Humidity", "Dwell Time", "Print Interval"], 36, 71)
        self.LabelsUnits(["", "INHGA", "INHG", "INHGA",
                         "INHGA", "INHGA", "HH:MM", "MM:SS"], 36)

        text36 = tk.Label(self.second_frame, text="GAS", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text36.grid(row=44, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Gas Pressure", "Pressure Increment", "Time Increment",
                    "Fast Increment Tolerance", "Print Interval", "Gas by Weight"], 45, 87)
        self.LabelsUnits(
            ["INHGA", "INHG", "MM:SS", "INHG", "MM:SS", "LBS"], 45)

        text43 = tk.Label(self.second_frame, text="GAS DWELL", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text43.grid(row=51, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Control Pressure", "Control Differential", "Dwell Time", "Maximum # Makeups", "Long Exposure", "Short Exposure",
                     "Hi Pressure", "Lo Pressure", "Hi Pressure Abort", "Emission Control Lead Time", "Print Interval"], 52, 94)
        self.LabelsUnits(["INHGA", "INHG", "HH:MM", "", "HH:MM",
                         "HH:MM", "INHGA", "INHGA", "INHGA", "HH:MM", "MM:SS"], 52)

        text55 = tk.Label(self.second_frame, text="AFTER VACUUM", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text55.grid(row=63, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Evacuation Pressure", "Anti-cavitation Pressure", "Air Interlock Pressure", "Pressure Increment", "Time Increment",
                     "Fast Increment Tolerance", "Slow Increment Termination Pressure", "Vacumm Hold Time", "Print Interval"], 64, 107)

        self.LabelsUnits(["INHGA", "INHGA", "INHGA", "INHG",
                         "MM:SS", "INHG", "INHGA", "HH:MM", "MM:SS"], 64)

        text65 = tk.Label(self.second_frame, text="GAS WASH A ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text65.grid(row=74, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["#Of Wash Cycles", "Release Type", "Release Pressure", "Evacuation Pressure", "Anti-cavitation Pressure", "Hi pressure",
                     "Release Pressure Increment", "Release Time Increment", "Release Fast Inc Tolerance", "Release Slow Increment Termination Pressure", "Release Hold Time",
                     "Vacuum Pressure Increment", "Vacuum Time Increment", "Vacuum Fast Inc Tolerance", "Vacuum Slow Increment Termination Pressure", "Vacuum Hold Time", "Print Interval"
                     ], 75, 117)

        self.LabelsUnits(["", "", "INHGA", "INHGA", "INHGA", "INHGA", "INHG", "MM:SS",
                         "INHG", "INHGA", "HH:MM", "INHG", "MM:SS", "INHG", "INHGA", "HH:MM", "MM:SS"], 75)

        text66 = tk.Label(self.second_frame, text="GAS WASH B ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text66.grid(row=93, column=2, sticky=tk.W, pady=5, padx=10)
        self.Labels(["#Of Wash Cycles", "Release Type", "Release Pressure", "Evacuation Pressure", "Anti-cavitation Pressure", "Hi pressure",
                     "Release Pressure Increment", "Release Time Increment", "Release Fast Inc Tolerance", "Release Slow Increment Termination Pressure", "Release Hold Time",
                     "Vacuum Pressure Increment", "Vacuum Time Increment", "Vacuum Fast Inc Tolerance", "Vacuum Slow Increment Termination Pressure", "Vacuum Hold Time", "Print Interval"
                     ], 94, 134)

        self.LabelsUnits(["", "", "INHGA", "INHGA", "INHGA", "INHGA", "INHG", "MM:SS",
                         "INHG", "INHGA", "HH:MM", "INHG", "MM:SS", "INHG", "INHGA", "HH:MM", "MM:SS"], 94)

        text67 = tk.Label(self.second_frame, text="RELEASE", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text67.grid(row=111, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Relsease Pressure", "Pressure Increment", "Time Increment", "Fast Increment Tolerance",
                     "Slow Increment Termination Pressure", "Print Interval"], 112, 169)

        self.LabelsUnits(
            ["INHGA", "INHG", "MM:SS", "INHG", "INHGA", "MM:SS"], 112)

        self.labels_entry()

        self.disable_edit()

        root.mainloop()
