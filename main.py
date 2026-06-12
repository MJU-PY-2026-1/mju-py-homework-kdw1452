#10개의 좌석 리스트 
seats = ["비어있음", "비어있음", "비어있음", "비어있음", "비어있음", "비어있음", "비어있음", "비어있음", "비어있음", "비어있음"]

#음식 메뉴와 가격 리스트
food_menu = ["라면", "김치 볶음밥", "탄산음료", "커피", "떡볶이" ,"핫도그"]
food_price = [3500, 5000, 2000, 2500, 5500, 3000]

cart = []
my_seat = -1
total_time = 0.0
total_payment = 0
today_revenue = 0
admin_pw = "1234"
user_names = []
user_times = []
users_info = []


#def 함수 정의

# 1-1. PC시간 충전(1000원에 1시간, 10,000원 이상 충전시 10,000원당 2시간 추가 이벤트)
def calculate_add_time(money) :
    add_time = money / 1000

    if money >= 10000 :
        print(f'{money}원 결제! 현재 진행중인 이벤트로 {(money // 10000) * 2}시간이 추가됩니다!')
        add_time += (money // 10000) * 2

    return add_time

# 1-2. PC 사용자 확인 및 시간 충전
def charge_time() : 
    global total_payment

    name = input('회원 이름을 입력하세요 : ')

    while True : 
        try :
            money = float(input('충전할 금액을 입력하세요 (원) : '))
            break
        
        except ValueError : 
            print(f'=> 금액은 숫자로만 입력해주세요.')

    charged_time = calculate_add_time(money)

    if name in user_names : 
        user_index = user_names.index(name)
        previous_time = user_times[user_index]
        user_times[user_index] = previous_time + charged_time

        print(f'=> {name}님! 다시 방문해주셔서 감사합니다.')
        print(f'=> 기존 {previous_time}시간 + 충전 {charged_time}시간')
        print(f'=> 총 잔여 시간 : {user_times[user_index]}시간 입니다')

    else :
        user_names.append(name)
        user_times.append(charged_time)

        print(f'=> {name}님 환영합니다! 신규 회원으로 등록되었습니다.')
        print(f'=> 총 잔여 시간 : {charged_time}시간')

    total_payment += money

# 2. 음식 주문 함수
def order_food() :
    global total_payment

    print()
    print('[음식 메뉴])')

    while True : 
        for i in range(6) : 
            print(f'{i+1}번 : {food_menu[i]} ({food_price[i]}원)')

        print('-' * 30)

        food_choice = int(input('주문 할 번호를 선택하세요 (0번 : 주문 완료 및 메인으로, 7번 : 장비구니 제거) : '))

        if 1 <= food_choice <= 6 :
            select_food = food_menu[food_choice - 1]
            select_price = food_price[food_choice - 1]

            cart.append(select_food)
            total_payment += select_price

            print(f'=> {select_food}이(가) 장바구니에 담겼습니다. (현재 장바구니 : {len(cart)}개)')

        elif food_choice == 0 :
            print(f'=> 음식 주문 종료 : 음식 주문을 완료하고 메인 메뉴로 돌아갑니다.')
            break

        elif food_choice == 7 :
            if len(cart) == 0 :
                print(f'=> 장바구니가 비어있어 제거할 메뉴가 없습니다.')

            print(f'현재 장바구니 : {cart}')
            remove_food = input('제거할 음식 메뉴 이름을 정확히 작성해 주세요 : ')

            if remove_food in cart : 
                cart.remove(remove_food)
                index = food_menu.index(remove_food)
                total_payment -= food_price[index]
                print(f' => {remove_food}이(가) 장바구니에서 제거되었습니다.')

            else : 
                print(f'=> 장바구니에 없는 메뉴입니다. 오타가 없는지 확인해주세요.')

        else : 
            print(f'=> 잘못된 번호입니다. 0~7번 사이의 숫자를 입력해주세요.')

# 3. 좌석 조회 및 좌석 선택 함수 
def select_seat() : 
    global my_seat

    print()
    print('[현재 좌석 현황]')

    for i in range(10) : 
        print(f'{i+1}번 좌석 {seats[i]}')

    name = input('좌석을 이용할 회원 이름을 입력해주세요 : ')

    if name not in user_names : 
        print(f'=> 등록되지 않은 회원입니다. 1번 메뉴에서 시간 충전을 먼저 해주세요.')
        return
    
    while True : 
        try:
            seat_choice = int(input('원하시는 좌석의 번호를 입력하세요(1~10) : '))
            break

        except ValueError : 
            print(f'좌석 번호는 숫자로만 입력해주세요. 다시 입력해주세요.')

    if 1 <= seat_choice <= 10 :
        seat_num = seat_choice - 1

        if seats[seat_num] == '비어있음' :
            seats[seat_num] = '사용중'
            my_seat = seat_num

            user_idx = user_names.index(name)
            users_info.append([name, user_times[user_idx], seat_choice, [] ])

            print(f'=> {seat_choice}번 좌석이 배정되었습니다!')

        else :
            print(f'=> 이미 사용중인 좌석입니다. 다른 좌석을 선택해주세요')

    else : 
        print(f'=> 잘못된 좌석 번호입니다.')
        
# 4. 내 정보 확인 및 장바구니 확인
def check_my_info() : 
    print()
    print('[내 정보 요약]')

    if my_seat == -1 :
        print('좌석 : 아직 선택하지 않았습니다.')

    else : 
        print(f'좌석 : {my_seat + 1}번 좌석 선택 됨')

    search_name = input('남은 시간을 조회할 이름을 입력하세요(없으면 엔터) : ')
    
    if search_name in user_names : 
        idx = user_names.index(search_name)
        print(f'{search_name}님의 남은 시간 : {user_times[idx]}시간')

    print('장바구니 목록 : ', end = '')
    if len(cart) == 0 :
        print('비어있음')

    else : 
        for item in cart : 
            print(f'[{item}]', end = '')
        print()

    print(f'현재 총 결제 금액 : {total_payment}원')
    print('-' * 30)


# 5. 연령 확인 및 결제 함수
def checkout_and_pay() : 
    global total_payment, today_revenue, my_seat, cart


    if total_payment == 0 :
        print(f'=> 결제하실 금액이 없습니다.')
        return

    print()
    print(f'결제 하실 금액은 총 {total_payment}원 입니다.')

    name = input(f'결재하시는 회원 이름을 입력해주세요 : ')

    print(f'주의 ! <야간에 미성년자가 출입을 시도하면 시스템 안전을 위해 기존 남은 시간까지 전량 몰수 및 회원 영구 제명 처리가 됩니다.>')
    while True : 
        time_check = input('현재 시간이 밤 10시 이후입니까? (네/아니요) : ')

        if time_check == '네' or time_check == '아니요' : 
            break

        else : 
            print(f'=> 정확히 "네" 또는 "아니요"만 입력해주세요.')

    if time_check == '네' : 
        while True : 
            try : 
                age = int(input(f'나이 확인을 위해 자신의 나이를 숫자로 입력해주세요 : ' ))
                break

            except ValueError : 
                print(f'나이는 숫자로만 입력해야 합니다. 다시 입력해주세요.')

        if age <= 19 :
            print(f' => 경고! 미성년자는 야간 출입이 불가합니다. 결제가 중지됩니다.')
            total_payment = 0
            cart = []

            if my_seat != -1 :
                seats[my_seat] = '비어있음'

                for user in users_info : 
                    if user[0] == name :
                        users_info.remove(user)

                my_seat = -1

            if name in user_names : 
                user_idx = user_names.index(name)
                user_names.pop(user_idx)
                user_times.pop(user_idx)

            return
        
        else : 
            print(f'=> 신분증 확인을 위해 입장하실 때, 카운터에 신분증을 제출해주세요.')

    for user in users_info : 
        if user[0] == name :
            user[3].extend(cart)

    print(f'=> 결제가 완료되었습니다. 감사합니다')
    today_revenue += total_payment
    total_payment = 0
    cart = []

# 6. 사용 종료 및 좌석 반납 함수
def end_use() : 
    global my_seat

    print()
    print('이용을 종료합니다.')

    name = input('종료하실 회원 이름을 입력해주세요 : ')

    target_user = []
    for user in users_info : 
        if user[0] == name :
            target_user = user
            break

    if len(target_user) > 0 : 
        return_seat = int(input('반납하실 좌석 번호를 입력해주세요(1~10) : '))

        if target_user[2] == return_seat  :
                use_time = float(input(f'오늘 사용하신 시간을 입력해주세요 : '))

                idx = user_names.index(name)
                user_times[idx] -= use_time

                seats[return_seat - 1] = '비어있음'
                my_seat = -1

                users_info.remove(target_user)


                print(f'=> {return_seat}번 좌석이 정상적으로 반납되었습니다. 안녕히 가세요!')

        else : 
                print(f'=> 좌석 번호가 일치하지 않습니다.')
    
    else : 
        print(f'=> 현재 좌석을 이용 중인 회원이 아니거나 이름을 잘못 입력하셨습니다.')

#7. 현재 이용자 정보 출력
def show_users_info() : 
    print()
    print(f'[현재 PC반 이용자 현황]')

    if len(users_info) == 0 :
        print(f'=> 현재 사용중인 회원이 없습니다.')
    
    else : 
        print(f'현재 사용중인 회원의 정보를 출력합니다. (회원이름, 남은 시간, 좌석번호, 주문한 음식)')
        print(f'-' * 30)

        for user in users_info :
            print(f'{user[0]}님의 남은 시간은 {user[1]}시간, 선택한 좌석은 {user[2]}번 입니다.', end = '')

            if len(user[3]) == 0 :
                print(f'주문한 음식 없음')

            else :
                for food in user[3] :
                    print(f'주문한 음식은 [{food}] 입니다.', end = '')

                print()



# 8. 관리자 메뉴 함수
def admin_menu() :
    pw_input = input('관리자 비밀번호를 입력하세요 : ')

    if pw_input == admin_pw : 
        print()
        print('[관리자 메뉴]')
        print(f'=> 오늘 총 누적 매출 : {today_revenue}')
        print('-' * 30)

    else :
        print('=> 비밀번호가 틀렸습니다')
            
#9. 텍스트 파일로 저장
def save_data() : 
        with open('users_info_backup.txt', 'w', encoding = 'utf-8') as file : 
            file.write(f'[현재 이용자 백업]')

            for user in users_info : 
                print(f'{user[0]} - {user[1]}시간, {user[2]}번 좌석, ' , end = '')

                if len(user[3]) == 0 :
                    print(f'주문한 음식 없음')

                else :
                    for food in user[3] : 
                        print(f'[{food}]' , end = '')

                    print()
        print(f'=> 현재 이용자 데이터의 백업이 텍스트 파일에 저장되었습니다.')                


#메인 프로그램 실행

print(f"PC방에 방문해주셔서 감사합니다. PC방 무인 키오스크 시스템을 시작합니다.")

while True :
    print('-' * 30)
    print('[메인 메뉴]')
    print('1. PC 시간 충전')
    print('2. 음식 주문')
    print('3. 좌석 조회 및 좌석 선택')
    print('4. 내 정보 확인 및 장바구니 확인')
    print('5. 연령 확인 및 최종 결제')
    print('6. 사용 종료 및 좌석 반납')
    print('7. 현재 이용자 현황 조회')
    print('8. [관리자 메뉴]')
    print('9. 데이터 파일 저장')
    print('10. 프로그램 종료')
    print('-' * 30)



    try : 
        num_choice = int(input('원하시는 메인 메뉴 번호를 입력하세요. : '))

    except ValueError : 
        print(f'=> 잘못된 입력입니다. 숫자만 입력해주세요.')
        continue


    if num_choice == 1 :
        charge_time()

    elif num_choice == 2 :
        order_food()

    elif num_choice == 3 :
        select_seat()

    elif num_choice == 4 :
        check_my_info()

    elif num_choice == 5 :
        checkout_and_pay()

    elif num_choice == 6 :
        end_use()

    elif num_choice == 7 :
        show_users_info()

    elif num_choice == 8 :
        admin_menu()

    elif num_choice == 9 :
        save_data()

    elif num_choice == 10 :
        print('=> PC반 키오스크 시스템을 안전하게 종료합니다.')
        save_data()
        break

    else :
        print('=> 잘못된 번호 입력입니다. 1~10번 까지 올바른 번호를 입력해주세요')
