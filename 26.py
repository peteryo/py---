while True:
    a=str(input("檢測的字串(end結束)"))
    if a=="end":
        print("檢測結束")
        break
    else:
        b=str(input("檢測單一字元"))
        print("字元"+b+"出現的次數為:",int(a.count(b)),"次")