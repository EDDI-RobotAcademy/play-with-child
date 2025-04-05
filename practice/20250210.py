class Person:
    def __init__(self, name, age, body, leukocyte, movement, virus, brain, face, poop, mom, dad,
                 eyes, ears, nose):

        self.name = name
        self.age = age
        self.body = body
        self.leukocyte = leukocyte
        self.movement = movement
        self.virus = virus
        self.brain = brain
        self.face = face
        self.poop = poop
        self.mom = mom
        self.dad = dad
        self.eyes = eyes
        self.ears = ears
        self.nose = nose

daniel = Person("이창희",8,"전쟁을 대비 하는 몸","힘샌 백혈구","댄스 하는 움직임"
                ,"감기","smart ", "good","very good poop",
                "김은혜","이상훈","예쁜 눈","good ears","일반 코")
angryMom = Person("김은혜",0,"불타는 몸",",약한 백혈구","댄스 하는 움직임"
                  ,"코로나,독감","bad brain","not good","very not golden poop normal poop",
                  "이숙희","김홍철","예쁜 눈 아직 까지 몰름","good ears","일반 코")

print(f"첫 번째 사람의 나이 = {daniel.age}, 이름 = {daniel.name}, 사람의 몸 = {daniel.body}, 백혈구 = {daniel.leukocyte}",
      f"움직임 = {daniel.movement}, virus = {daniel.virus}, brain = {daniel.brain}\n",
      f"좋은 얼굴 = {daniel.face}, 좋은 똥은 = {daniel.poop}, mom = {daniel.mom},dad = {daniel.dad},eyes = {daniel.eyes}\n",
      f"귀 = {daniel.ears},사람이 코 = {daniel.nose}")
print(f"두번째 사람의 나이 = {angryMom.age}, 이름 = {angryMom.name}, 사람의 몸 = {angryMom.body}, 백혈구 = {angryMom.leukocyte}",
      f"움직임 = {angryMom.movement}, virus = {angryMom.virus}, brain = {angryMom.brain}\n",
      f"못새긴 얼굴 = {angryMom.face},그냥 똥 = {angryMom.poop},mom = {angryMom.mom},dad = {angryMom.dad},eyes = {angryMom.eyes}\n",
      f"귀 = {angryMom.ears},사람이 코 = {angryMom.nose}")
