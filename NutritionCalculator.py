import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("몸을 위한 영양분 계산기")

        self.pushButton = QPushButton("신체 수치를 입력하세요")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    
    def pushButtonClicked(self):
        height, ok = QInputDialog.getDouble(self, '키 입력', '사용자의 키를 입력하세요.(cm)')
        if ok:
            self.height = height
            self.label.setText(str(height))
            
        kg, ok2 = QInputDialog.getDouble(self, '몸무게 입력', '사용자의 몸무게를 입력하세요.(kg)')
        if ok2:
            self.kg= kg 
            self.label.setText(str(kg))
            
        gender, ok3 = QInputDialog.getText(self, '성별 입력', '사용자의 성별을 여자면 F, 남자면 M으로 입력하세요.')
        while gender != 'F' and gender != 'M':
            gender, ok3 = QInputDialog.getText(self, '성별 입력', '사용자의 성별을 여자면 \'F\', 남자면 \'M\'으로 입력하세요!')
        if ok3:
            self.gender = gender

        age, ok4 = QInputDialog.getInt(self, '나이 입력', '사용자의 나이를 입력하세요(만)')
        if ok4:
            self.age = age
            self.label.setText("이 창을 닫으면 사용자에게 맞는 영양분 섭취량을 파일로 보여줍니다. 확인해 보세요!")
        
                    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


#######################################

Height, Kg, Gender, Age = window.height, window.kg, window.gender, window.age

print(Height, Kg, Gender, Age)

def BMR_Calculator(): # Bmr : 기초대사량 
    if Gender == 'M':
        s = 5
    else:
        s = -161
    
    BMR = 10*Kg + 6.25*Height - 5*Age + s
    
    return BMR  # 추정치임


def Activity_Calculator():  # 활동대사량 
    bmr = BMR_Calculator()
    
    act_sedentary = bmr *0.2
    act_light_active = bmr*0.375
    act_moderately_active = bmr*0.55
    act_very_active = bmr*0.725
    act_extra_active = bmr*0.9

    return int(act_sedentary), int(act_light_active), int(act_moderately_active), int(act_very_active), int(act_extra_active)


def Total_Consume(): #총 하루 필요 열량 
    bmr = BMR_Calculator()

    Total_sedentary = bmr * 1.2 #거의 앉아있거나 안 움직임 
    Total_light_active = bmr * 1.375 # 간단한 운동/ 주마다 1~3번 운동 
    Total_moderately_active = bmr * 1.55 #적당한 운동 / 주마다 3~5번 운동
    Total_very_active = bmr * 1.725 #강한 운동 / 주마다 6~7번 운동
    Total_extra_active = bmr * 1.9 # 신체 쓰는 일 있는 사람 or 트레이닝 강도 2배 

    return int(Total_sedentary), int(Total_light_active), int(Total_moderately_active), int(Total_very_active), int(Total_extra_active)

                    
def ProteinCalculator(): # 단백질 섭취 필요량 
    Minimum = Kg * 1.2 # 대사량 근육량 유지하는 최소 필요량
    Lower = Kg * 1.4 #식욕 감소 효과 
    Medium = Kg * 1.6 # 체중, 체지방 감량 촉진. 동시에 근육량 보존해주는 이상적인 필요량 
    High = Kg*1.8  #근육량 많은 운동선수들이 단기간 다이어트 시 근손실 방지해주는 필요량 
    High2 = Kg*2.3    #운동선수 근손실 방지 범위 최대
    
    return int(Minimum), int(Lower), int(Medium), int(High), int(High2)
    

def CarbCalculator(): # 탄수화물 섭취 필요량 
    total = Total_Consume()

    CarbSedentary1 = total[0] * 0.45 /4
    CarbSedentary2 = total[0] * 0.65 /4

    CarbLightActive1 = total[1] * 0.45 /4
    CarbLightActive2 = total[1] * 0.65 /4
    
    CarbModeratelyActive1 = total[2] * 0.45 /4
    CarbModeratelyActive2 = total[2] * 0.65 /4
    
    CarbVeryActive1 = total[3] * 0.45 /4
    CarbVeryActive2 = total[3] * 0.65 /4

    CarbExtraActive1 = total[4] * 0.45 /4
    CarbExtraActive2 = total[4] * 0.65 /4

    return int(CarbSedentary1), int(CarbSedentary2), int(CarbLightActive1), int(CarbLightActive2), int(CarbModeratelyActive1), int(CarbModeratelyActive2), int(CarbVeryActive1), int(CarbVeryActive2), int(CarbExtraActive1), int(CarbExtraActive2)
    

def FatCalculator(): # 지방 섭취 필요량 
    
    total = Total_Consume()

    FatSedentary1 = total[0] * 0.2 /9
    FatSedentary2 = total[0] * 0.35 /9

    FatLightActive1 = total[1] * 0.2 /9
    FatLightActive2 = total[1] * 0.35 /9
    
    FatModeratelyActive1 = total[2] * 0.2 /9
    FatModeratelyActive2 = total[2] * 0.35 /9
    
    FatVeryActive1 = total[3] * 0.2 /9
    FatVeryActive2 = total[3] * 0.35 /9

    FatExtraActive1 = total[4] * 0.2 /9
    FatExtraActive2 = total[4] * 0.35 /9
    
    return int(FatSedentary1), int(FatSedentary2), int(FatLightActive1), int(FatLightActive2), int(FatModeratelyActive1), int(FatModeratelyActive2), int(FatVeryActive1), int(FatVeryActive2), int(FatExtraActive1), int(FatExtraActive2)


BMR = BMR_Calculator()
Activity = Activity_Calculator()
Total = Total_Consume()
Protein = ProteinCalculator()
Carbon = CarbCalculator()
Fat = FatCalculator()

print(BMR, Activity, Total, Protein, Carbon, Fat)


if Gender == 'M':
    genderforWrite = 'Male'
else:
    genderforWrite = 'Female'

with open("영양분 섭취량 정리.txt","w") as file:
    file.write("사용자의  키 :"+str(Height)+'cm'+"  몸무게 : "+str(Kg)+'kg'+"  성별 : "+genderforWrite+ "  나이 : "+ str(Age)+'\n\n')
    
    file.write("※다음 값들은 추정치입니다. 그러니 참고용으로 활용해주시면 됩니다!\n\n")
    
    file.write("기초 대사량(BMR: 생명 활동에 필요한 최소 에너지 소모량): "+'약 '+str(BMR)+'kcal\n\n') # 기초 대사량
    
    file.write("활동 대사량(활동하는 데 필요한 에너지 소모량):\n") # 활동 대사량 
    file.write("별 다른 운동 없이 앉아만 있는 경우 : "+str(Activity[0])+'kcal'+'\n')  
    file.write("매주 1~3번 간단한 운동을 하는 경우 : "+str(Activity[1])+'kcal'+'\n')
    file.write("매주 3~5번 적당한 운동을 하는 경우 : "+str(Activity[2])+'kcal'+'\n')
    file.write("매주 6~7번 강도있는 운동을 하는 경우 : "+str(Activity[3])+'kcal'+'\n')
    file.write("매우 고강도 운동을 하거나 신체를 쓰는 직업을 삼고있는 경우 : "+str(Activity[4])+'kcal'+'\n\n')

    file.write("하루 총 필요 열량:\n") # 총 열량 
    file.write("별 다른 운동 없이 앉아만 있는 경우 : "+str(Total[0])+'kcal'+'\n')  
    file.write("매주 1~3번 간단한 운동을 하는 경우 : "+str(Total[1])+'kcal'+'\n')
    file.write("매주 3~5번 적당한 운동을 하는 경우 : "+str(Total[2])+'kcal'+'\n')
    file.write("매주 6~7번 강도있는 운동을 하는 경우 : "+str(Total[3])+'kcal'+'\n')
    file.write("매우 고강도 운동을 하거나 신체를 쓰는 직업을 삼고있는 경우 : "+str(Total[4])+'kcal'+'\n')
    file.write("(다이어트시 총 열량에 약 -500kcal, 벌크업의 경우 약 +200~300kcal)\n\n")

    file.write("1일 단백질 섭취량:\n") # 단백질
    file.write("대사량과 근육량을 유지해주는 최소 필요량 : "+str(Protein[0])+'g'+'\n')  
    file.write("식욕 감소 효과 : "+str(Protein[1])+'g'+'\n--여기까지 식이요법 병행 시 추천'+'\n')
    file.write("체중, 체지방 감량 촉진. 동시에 근육량 보존해주는 이상적인 필요량 : "+str(Protein[2])+'g'+'\n')
    file.write("근육량 많은 운동선수들이 단기간 다이어트 시 근손실 방지해주는 필요량 : "+str(Protein[3])+'~'+str(Protein[4])+'g'+'\n--근력운동 병행 시 추천'+'\n\n')

    file.write("1일 탄수화물 섭취량:\n") # 탄수화물
    file.write("(※탄수화물 섭취 열량은 전체 섭취 열량의 45%~65%가 보통이지만 다이어트를 진행할 경우 해당 추정값보다 낮게 드시면 됩니다.)\n") #이거 kcal말고 g으로 바꿔줘야됨
    file.write("별 다른 운동 없이 앉아만 있는 경우 : "+str(Carbon[0])+'~'+str(Carbon[1])+'g'+'\n')
    file.write("매주 1~3번 간단한 운동을 하는 경우 : "+str(Carbon[2])+'~'+str(Carbon[3])+'g'+'\n')
    file.write("매주 3~5번 적당한 운동을 하는 경우 : "+str(Carbon[4])+'~'+str(Carbon[5])+'g'+'\n')
    file.write("매주 6~7번 강도있는 운동을 하는 경우 : "+str(Carbon[6])+'~'+str(Carbon[7])+'g'+'\n')
    file.write("매우 고강도 운동을 하거나 신체를 쓰는 직업을 삼고 있는 경우 : "+str(Carbon[8])+'~'+str(Carbon[9])+'g'+'\n\n') 
    
    file.write("1일 지방 섭취량:\n") #지방
    file.write("별 다른 운동 없이 앉아만 있는 경우 : "+str(Fat[0])+'~'+str(Fat[1])+'g'+'\n')
    file.write("매주 1~3번 간단한 운동을 하는 경우 : "+str(Fat[2])+'~'+str(Fat[3])+'g'+'\n')
    file.write("매주 3~5번 적당한 운동을 하는 경우 : "+str(Fat[4])+'~'+str(Fat[5])+'g'+'\n')
    file.write("매주 6~7번 강도있는 운동을 하는 경우 : "+str(Fat[6])+'~'+str(Fat[7])+'g'+'\n')
    file.write("매우 고강도 운동을 하거나 신체를 쓰는 직업을 삼고 있는 경우 : "+str(Fat[8])+'~'+str(Fat[9])+'g'+'\n\n') 
            







    
     
    
    
