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
    money = float(input('충전할 금액을 입력하세요 (원) : '))

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

    seat_choice = int(input('원하시는 좌석의 번호를 입력하세요(1~10) : '))

    if 1 <= seat_choice <= 10 :
        seat_num = seat_choice - 1

        if seats[seat_num] == '비어있음' :
            seats[seat_num] = '사용중'
            my_seat = seat_num
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

    print()
    print(f'결제 하실 금액은 총 {total_payment}원 입니다.')

    time_check = input('현재 시간이 밤 10시 이후입니까? (네/아니요) : ')

    if time_check == '네' : 
        age = int(input(f'나이 확인을 위해 자신의 나이를 숫자로 입력해주세요 : ' ))
        
        if age <= 19 :
            print(f' => 경고! 미성년자는 야간 출입이 불가합니다. 결제가 중지됩니다.')
            total_payment = 0
            cart = []

            if my_seat != -1 :
                seats[my_seat] = '비어있음'
                my_seat = -1

            return
        
        else : 
            print(f'=> 신분증 확인을 위해 입장하실 때, 카운터에 신분증을 제출해주세요.')

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

    if name in user_names : 
        return_seat = int(input('반납하실 좌석 번호를 입력해주세요(1~10) : '))

        if 1 <= return_seat <= 10 :
            return_index = return_seat - 1

            if seats[return_index] == '사용중' : 
                user_index = user_names.index(name)
                
                use_time = float(input('오늘 사용하신 시간을 입력해주세요 : '))

                current_time = user_times[user_index]
                updated_time = current_time - use_time
                user_times[user_index] = updated_time 

                seats[return_index] = '비어있음'
                my_seat = -1

                print(f'=> {return_seat}번 좌석이 정상적으로 반납되었습니다.')
                print(f'=> {name}님, 남은 시간은 {updated_time}시간 입니다. 안녕히 가세요!')

            else : 
                print(f'=> {return_seat}번 좌석은 현재 비어있습니다. 본인의 좌석번호를 확인해주세요')

        else :
            print(f'=> 잘못된 좌석 번호입니다. 1~10 사이의 숫자를 입력해주세요.')

    else :
        print(f'=> 등록되지 않은 이름입니다. 이름을 확인해주세요.')

# 7. 관리자 메뉴 함수
def admin_menu() :
    pw_input = input('관리자 비밀번호를 입력하세요 : ')

    if pw_input == admin_pw : 
        print()
        print('[관리자 메뉴]')
        print(f'=> 오늘 총 누적 매출 : {today_revenue}')
        print('-' * 30)

    else :
        print('=> 비밀번호가 틀렸습니다')
            
    


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
    print('7. [관리자 메뉴]')
    print('8. 프로그램 종료')
    print('-' * 30)

    num_choice = int(input('원하시는 메인 메뉴 번호를 입력하세요. : '))

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
        admin_menu()

    elif num_choice == 8 :
        print('=> PC반 키오스크 시스템을 안전하게 종료합니다.')
        break

    else :
        print('=> 잘못된 번호 입력입니다. 1~8번 까지 올바른 번호를 입력해주세요')
