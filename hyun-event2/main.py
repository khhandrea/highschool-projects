import firebase_admin
from firebase_admin import credentials, firestore
import csv
from datetime import datetime
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
from random import randrange
from time import sleep

font_name = font_manager.FontProperties(fname="malgunbd.ttf").get_name()
rc('font', family=font_name)

window_size = "400x400"
message_font_size = 21
button_font_size = 15
users_font_size = 12

def button1_clicked():
  message.config(text = '\nsaving data...\n', fg='black')
  
  ##fetch data
  try:
    users_ref = db.collection(u'event2')
    docs = users_ref.stream()

    ##write .csv
    #now = datetime.today().strftime("%Y%m%d_%H:%M:%S")
    #f = open(f'data-{now}.csv', 'w', encoding='utf-8', newline='')
    f = open(f'sample.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    for doc in docs:
      wr.writerow([
        doc.to_dict()['date'],
        doc.to_dict()['number'], 
        doc.to_dict()['item'],
        doc.to_dict()['answer'][0], 
        doc.to_dict()['answer'][1],
        doc.to_dict()['answer'][2],
        doc.to_dict()['answer'][3]
      ])
    f.close()
  except:
    message.config(text = '\nfetch error\n', fg='red')
  else:
    message.config(text = '\n.csv saved\n', fg='black')
    try:
      #current users
      f = open(f'sample.csv', 'r', encoding='utf-8', newline='')
      rdr = csv.reader(f)
      _data_ = []
      for line in rdr:
        _data_.append(line[1])
      f.close()
      message2.config(text = f'\n참여자 : {len(_data_)}명\n', fg='black')
    except:
      message2.config(text = '\nfetch error\n', fg='red')

  
def button2_clicked():
  message.config(text = "\nreading data...\n", fg='black')
  
  ##read .csv
#try:
  f = open(f'sample.csv', 'r', encoding='utf-8', newline='')
  rdr = csv.reader(f)
  _data_ = [
      [0, 0, 0], #grade
      [0, 0], #choose
      [0, 0], #gender
      [0, 0, 0, 0, 0], #Q1
      [0, 0, 0, 0], #Q2
      [0, 0, 0], #Q3
      [0, 0], #moon/lee
      [0, 0], #moon
      [0, 0] #lee
    ]
  for line in rdr:
    for i in range(1, 6):
      _data_[0][int(line[1][0])-1] += 1 #grade
      _data_[i][int(line[i+1])] += 1
    if(int(line[1][0]) == 1): #moon/lee
      grade = int(line[1][1])*10 + int(line[1][2])
      if(grade <= 6):
        _data_[6][0] += 1
        _data_[7][int(line[2])] += 1
      else:
        _data_[6][1] += 1
        _data_[8][int(line[2])] += 1
  f.close()

  message.config(text = '\nplotting graphs...\n', fg='black')
  
  ##plot
  ##grade
  categories = ['1학년', '2학년', '3학년']
  plt.subplot(331)
  #plt.legend(categories)
  plt.title('학년')
  plt.pie(_data_[0],
          labels=categories,
          explode=(0.01, 0.01, 0.01))
  
  ##choose
  categories = ['데상트', '나이키']
  plt.subplot(332)
  #plt.legend(categories)
  plt.title('데상트 후드 vs 나이키 후드')
  plt.pie(_data_[1],
          labels=categories,
          autopct='%.1f%%',
          colors=['#487eb0', '#dcdde1'],
          explode=(0.01, 0.01))

  ##gender
  categories = ['남', '여']
  plt.subplot(333)
  plt.title('성별')
  plt.pie(_data_[2],
          labels=categories,
          autopct='%.1f%%',
          colors=['#aaaaaa', '#aaaaaa'],
          explode=(0.01, 0.01))
   ##Q1
  categories = ['90', '95', '100', '105', '110']
  plt.subplot(334)
  plt.title('사이즈')
  plt.pie(_data_[3],
          labels=categories,
          colors=['#cccccc', '#bbbbbb', '#aaaaaa', '#999999', '#888888'],
          explode=(0.01, 0.01, 0.01, 0.01, 0.01))
   ##Q2
  categories = ['버스', '지하철', '도보', '기타']
  plt.subplot(335)
  plt.title('등교')
  plt.pie(_data_[4],
          labels=categories,
          explode=(0.01, 0.01, 0.01, 0.01),
          colors=['#fad390', '#60a3bc', '#78e08f', '#aaaaaa'])
   ##Q3
  categories = ['안경', '렌즈', '둘 다 x']
  plt.subplot(336)
  plt.title('안경 vs 렌즈')
  plt.pie(_data_[5],
          labels = categories,
          autopct='%.1f%%',
          colors=['#9c88ff', '#00a8ff', '#dcdde1'],
          explode=(0.01, 0.01, 0.01))
   ##moon/lee
  categories = ['문과', '이과']
  plt.subplot(337)
  plt.title('2학년')
  plt.pie(_data_[6],
          labels=categories,
          explode=(0.01, 0.01),
          autopct='%.1f%%',
          colors=['#badc58', '#c7ecee'])
   ##moon
  categories = ['나이키', '데상트']
  plt.subplot(338)
  plt.title('문과')
  plt.pie(_data_[6],
          labels=categories,
          explode=(0.01, 0.01),
          autopct='%.1f%%',
          colors=['#487eb0', '#dcdde1'])
   ##lee
  categories = ['나이키', '데상트']
  plt.subplot(339)
  plt.title('이과')
  plt.pie(_data_[7],
          labels=categories,
          explode=(0.01, 0.01),
          autopct='%.1f%%',
          colors=['#487eb0', '#dcdde1'])
  
  plt.show()
#except:
#    message.config(text = '\nfetch error\n', fg='red')

def button3_clicked():
  message.config(text = "\nreading data...\n", fg='black')
  
  ##read .csv
  try:
    f = open(f'sample.csv', 'r', encoding='utf-8', newline='')
    rdr = csv.reader(f)
    _data_ = []
    for line in rdr:
      _data_.append([line[1], line[2]])
    f.close()
    rand_num = randrange(1, len(_data_))
    user = _data_[rand_num][0]
    item = "나이키 후드티" if _data_[rand_num][1] == "0" else "데상트 후드티"
    message.config(text = f'\n{user}, {item}\n', fg='black')
  except:
      message.config(text = '\nfetch error\n', fg='red')

##initialize firebase fetch
cred = credentials.Certificate('./serviceAccount.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

##create tk
root = tk.Tk()
root.configure(bg='#eeeeee')
root.title("보정고 이벤트")
root.geometry(f"{window_size}+200+200")

##message
#main message
message = tk.Label(root, text = '\nchoose an action\n', font=('malgunbd.ttf', message_font_size))
message = tk.Label(root, text = '\nchoose an action\n', font=('malgunbd.ttf', message_font_size))

#current users
message2 = tk.Label(root, text = "\nloading data...\n", font=('malgun.ttf', users_font_size))
try:
  f = open(f'sample.csv', 'r', encoding='utf-8', newline='')
  rdr = csv.reader(f)
  _data_ = []
  for line in rdr:
    _data_.append(line[1])
  f.close()
  message2.config(text = f'\n참여자 : {len(_data_)}명\n', fg='black')
except:
  message2.config(text = '\nfetch error\n', fg='red')

##button
button1 = tk.Button(root,
                    text = 'save .csv file',
                    command = button1_clicked,
                    width=15,
                    fg='#ffffff',
                    bg='#0984e3',
                    borderwidth=0,
                    relief='solid',
                    font=('malgunbd.ttf', button_font_size)
                    )
button2 = tk.Button(root,
                    text = 'show graphs',
                    command = button2_clicked,
                    width=15,
                    fg='#ffffff',
                    bg='#00b894',
                    borderwidth=0,
                    relief='solid',
                    font=('malgunbd.ttf', button_font_size)
                    )
button3 = tk.Button(root,
                    text = 'click!',
                    command = button3_clicked,
                    width=15,
                    fg='#ffffff',
                    bg='#fd79a8',
                    borderwidth=0,
                    relief='solid',
                    font=('malgunbd.ttf', button_font_size)
                    )
margin1 = tk.Label(root, text = ' ')
margin2 = tk.Label(root, text = ' ')

message.pack()
button1.pack()
margin1.pack()
button2.pack()
margin2.pack()
button3.pack()
message2.pack()

##run tk
root.mainloop()
