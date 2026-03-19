import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")
df['date'] = pd.to_datetime(df['date'])

print(df.head)

#categorizing by type
def byCategory(df, category):
    return df[df["type"] == category]['amount'].sum()
    
#categorizing by date
def byDate(df, date):
    return df[df["date"] == date]['amount'].sum()

#menu
def menu():
    print("1. Total Spending")
    print("2. Category Total")
    print("3. Date Total")
    print("4. Monthly total")
    print("5. Total Expenses Chart")
    print("6. Comparison chart")
    print("7. Exit")
 
menu()
 
while True:
    choice = input("\nEnter choice number from menu: ")
    
    if choice == '1':
        print("Total Spending : Rs.", df['amount'].sum())
        
    elif choice == '2':
        print("Available categories: ",df['type'].unique())
        category_input = input("Enter category: ").lower()
        
        if category_input in df['type'].unique():
            print(f"{category_input} total: Rs.", byCategory(df, category_input))
        else:
            print("Invalid category")
            
    elif choice == '3':
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            date = pd.to_datetime(date_input)
            print(f"{date_input} total: Rs.", byDate(df, date_input))
        except:
            print("Invalid date")
            
    elif choice == '4':
        month_input = input("Enter month (YYYY-MM): ")
        
        try: 
            selected_month = pd.Period(month_input, freq="M")
        except:
            print("Invalid month format")
            continue
            
        df["month"] = df["date"].dt.to_period("M")
        filtered = df[df['month'] == selected_month]
        
        if filtered.empty:
            print("No data for this month")
        else:
            print(f"{month_input} total: Rs.",filtered['amount'].sum())
            
        
    elif choice == '5':
        totals = df.groupby('type')['amount'].sum()
        
        plt.bar(totals.index, totals.values)
        plt.xlabel("Category")
        plt.xticks(rotation=30)
        plt.ylabel("Amount (Rs.)")
        plt.title("Expenses by Category")
        plt.grid(axis='y', zorder=0)
        plt.show()
    
    elif choice == '6':
        monthly_totals = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
        monthly_totals = monthly_totals.sort_index()
        monthly_totals.index = monthly_totals.index.to_timestamp()
        plt.plot(monthly_totals.index, monthly_totals.values, '--b', marker='o')
        plt.title("Monthly Expense Trend")
        plt.xlabel("Month")
        plt.ylabel("Amount (Rs.)")
        plt.xticks(rotation=35)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
       
       
    elif choice == '7':
        print("Exiting...")
        break
        
    else:
        print("Invalid choice")
        
    
   

