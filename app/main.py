from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


class Monster:
    def __init__(self, name, health, attack_power, species):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.species = species

    def __str__(self):
        return (f"이름: {self.name}\n"
                f"체력: {self.health}\n"
                f"공격력: {self.attack_power}\n"
                f"종족: {self.species}")

    def attack(self, target):
        if target.health > 0:
            target.health -= self.attack_power
            print(f"{self.name}이(가) {target.name}을(를) 공격했습니다! {target.name}의 남은 체력: {target.health}")
            if target.health <= 0:
                print(f"{target.name}이(가) 쓰러졌습니다!")
        else:
            print(f"{target.name}은(는) 이미 쓰러진 상태입니다.")

# 객체 생성
tutorialBoss = Monster(name="튜토리얼보스", health=100, attack_power=20, species="휴먼")
zombie = Monster(name="좀비", health=5, attack_power=10, species="언데드")
knight = Monster(name="근위기사", health=25, attack_power=10, species="휴먼")
wyvern = Monster(name="와이번", health=30, attack_power=25, species="드래곤")
dark_knight = Monster(name="암흑기사", health=30, attack_power=30, species="언데드")
skeleton_archer = Monster(name="스켈레톤 아처", health=5, attack_power=15, species="언데드")

# 출력
unit_list = [zombie, knight, wyvern, dark_knight, skeleton_archer]
ally_list = []
enemy_list = [tutorialBoss]

while True:
    print("\n[메뉴 선택]")
    print("1번: 공격")
    print("2번: 유닛 출전")
    print("3번: 적군과 아군 유닛 리스트 보기")
    print("4번: 종료")

    choice = input("선택하세요: ")

    if choice == "1":
        if not ally_list:
            print("\n아군이 없습니다. 먼저 유닛을 출전시키세요.")
            continue

        print("\n공격할 대상을 선택하세요:")
        print("1. 적")
        print("2. 아군")
        target_group = input("대상 그룹을 선택하세요: ")

        if target_group == "1" and enemy_list:
            print("\n공격할 적을 선택하세요:")
            for idx, enemy in enumerate(enemy_list, start=1):
                print(f"{idx}. {enemy.name} (체력: {enemy.health})")
            target_idx = input("공격할 적 번호를 입력하세요: ")

            if target_idx.isdigit() and 1 <= int(target_idx) <= len(enemy_list):
                target = enemy_list[int(target_idx) - 1]
                ally_list[0].attack(target)
                if target.health <= 0:
                    enemy_list.remove(target)
            else:
                print("\n잘못된 선택입니다.")

        elif target_group == "2" and ally_list:
            print("\n공격할 아군을 선택하세요:")
            for idx, ally in enumerate(ally_list, start=1):
                print(f"{idx}. {ally.name} (체력: {ally.health})")
            target_idx = input("공격할 아군 번호를 입력하세요: ")

            if target_idx.isdigit() and 1 <= int(target_idx) <= len(ally_list):
                target = ally_list[int(target_idx) - 1]
                ally_list[0].attack(target)
                if target.health <= 0:
                    ally_list.remove(target)
            else:
                print("\n잘못된 선택입니다.")
        else:
            print("\n대상이 존재하지 않거나 잘못된 입력입니다.")

    elif choice == "2":
        print("\n출전 가능한 유닛 리스트:")
        for idx, unit in enumerate(unit_list, start=1):
            print(f"{idx}. {unit.name} (체력: {unit.health})")

        unit_idx = input("출전할 유닛 번호를 입력하세요: ")

        if unit_idx.isdigit() and 1 <= int(unit_idx) <= len(unit_list):
            selected_unit = unit_list.pop(int(unit_idx) - 1)
            ally_list.append(selected_unit)
            print(f"\n{selected_unit.name}이(가) 출전했습니다!")
        else:
            print("\n잘못된 선택입니다.")

    elif choice == "3":
        # 적군 리스트 출력
        print(Fore.RED + "\n적군 리스트:")
        for enemy in enemy_list:
            print(Fore.GREEN + str(enemy))

        # 아군 리스트 출력
        print(Fore.RED + "\n아군 리스트:")
        for ally in ally_list:
            print(Fore.GREEN + str(ally))

    elif choice == "4":
        print("\n게임을 종료합니다.")
        break

    else:
        print("\n잘못된 입력입니다. 다시 선택하세요.")
