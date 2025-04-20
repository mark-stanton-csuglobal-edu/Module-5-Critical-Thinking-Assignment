# Part 1: collect data and calculate the average rainfall over a period of years
def main():
    # Variables for annual loop
    y = 1
    annual_inches = []

    # User enters the number of years for which we will be calculating
    years = int(input("Enter the number of years we will be calculating average rainfall for: "))

    # Annual loop
    while y <= years:
        # Create variables for monthly loop
        m = 1
        monthly_inches = []
        # Monthly loop
        while m <= 12:
            monthly_inches.append(float(input('Enter the average rainfall for this month in inches: ')))
            # increment m control variable
            m += 1

        # Append the sum of the 12 months just entered to the annual list
        annual_inches.append(sum(monthly_inches))

        # increment y control variable
        y += 1

    # Display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period
    print('Total number of months: ' + str(years * 12))
    print('Total inches of rainfall for this period: ' + str(sum(annual_inches)) + ' inches')
    print('Average Rainfall per month for this period is: ' + str(round((sum(annual_inches)) / (years * 12),2)) + ' inches')
main()

# Part 2: Display book club points for the month
def main():
    # User enters the number of books purchased this month
    numBooks = int(input('Please enter the number of books you have purchased this month: '))

    # if/else statement checks for 8+ books
    if numBooks >= 8:
        print('You have earned 60 points')
    else:
        # if/else statement checks for 6/7 books
        if numBooks >= 6:
            print('You have earned 30 points')
        else:
            # if/else statement checks for 4/5 books
            if numBooks >= 4:
                print('You have earned 15 points')
            else:
                # if/else statement checks for 2/3 books
                if numBooks >= 2:
                    print('You have earned 5 points')
                else:
                    # remaining case is for 0/1 book
                    print('You have earned 0 points')
main()
