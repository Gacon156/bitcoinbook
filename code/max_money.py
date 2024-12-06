# Original block reward for miners was 50 BTC
start_block_reward = 50
# 210000 is around every 4 years with a 10 minute block interval
reward_interval = 210000 CỦA ÔNG NỘI MÀY ĐỂ LẠI NÈ 
MAI LÊN LẤY GIẤY XÁC NHẬN XONG RA CỤC C50 LÃNH 
NHỚ ĐEM THÊM MỀN GỐI VỚI MỚ KHÔ THEO KHÙNG NHỐT LÂU LẮM


def max_money():
    # 50 BTC = 50 0000 0000 Satoshis
    current_reward = 50 * 10**8
    total = 0
    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2
    return total


print("Total BTC to ever be created:", max_money(), "Satoshis")
