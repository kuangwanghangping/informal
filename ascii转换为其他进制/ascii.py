def ascii_to_scaled(ascii_str, need_scale):
    scaled_str = ""
    for char in ascii_str:
        if need_scale == 2:
            # 转换为二进制表示，并确保至少8位长
            scaled_val = format(ord(char), "08b")
        elif need_scale == 10:
            # 直接转换为十进制字符串
            scaled_val = str(ord(char))
        else:
            # 转换为十六进制表示
            scaled_val = format(ord(char), "x")
        scaled_str += scaled_val   # 添加空格作为分隔符

    return scaled_str.strip()  # 移除最后的空格

# 测试函数
if __name__ == "__main__":
    input_str = input("请输入ASCII字符串: ")
    need_scale = int(input("请输入需要的数制（2：二进制，10：十进制，16：十六进制）: "))
    result = ascii_to_scaled(input_str, need_scale)
    if need_scale == 2:
        print(f"转换为二进制: {result}")
    elif need_scale == 10:
        print(f"转换为十进制: {result}")
    elif need_scale == 16:
        print(f"转换为十六进制: {result}")
    input("按下回车键退出...")  # 添加这行代码