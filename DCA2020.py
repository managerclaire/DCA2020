def filing_status():
    fsinput = input("Did you file married filing jointly? Y/N: ")
    if fsinput == "Y":
        fs = "MFJ"
    else:
        fs = "S"
    return fs
print("You will need your 2018 tax return. Please fetch it now.")
fs = filing_status()
def count_children():
    children = int(input("How many children do you have? "))
    return children
children = count_children()
def line_seven():
    line = int(input("Please enter the number in line 7 from page 1 of your Form 1040: "))
    return line
agi = line_seven()
def net_income_tax_liability():
    line_eleven = int(input("Please enter the number in line 11: "))
    line_twelve = int(input("Please enter the number in line 12: "))
    line_thirteen = line_eleven - line_twelve
    line_seventeen = int(input("Please enter the number in line 17: "))
    nitl = line_thirteen - line_seventeen
    print("Your net income tax liability in 2018 was $",nitl)
    return nitl
nitl = net_income_tax_liability()
def dca_calculation(filing, child, agi, nitl):
    filing = filing
    child = child
    agi = agi
    nitl = nitl
    child_benefit = child*500
    if filing == "MFJ":
        if agi <= 150000:
            if nitl <= 2400:
                base = max(1200,nitl)
                total_dca = base+child_benefit
            else:
                base = min(2400,nitl)
                total_dca = base+child_benefit
        else:
            base = min(2400,nitl)
            next_step = base+child_benefit
            total_dca = next_step-(.05*(agi-150000))
    else:
        if agi <= 75000:
            if nitl <= 1200:
                base = max(600,nitl)
                total_dca = base+child_benefit
            else:
                base = min(1200,nitl)
                total_dca = base+child_benefit
        else:
            base = min(2400,nitl)
            next_step = base+child_benefit
            total_dca = next_step-(.05*(agi-75000))
    return total_dca
dca = dca_calculation(fs, children, agi, nitl)
print("Your calculated direct cash assitance would be: $",dca)


