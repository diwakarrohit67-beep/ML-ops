class chatbook:
    def __init__(self):
        self.username =  ''
        self.password = ''
        self.email = ''
        self.loggdin = False
        self.menu()
        
    def menu(self):
        user_input = input("Welcome to ChatBook! Please choose an option:\n1. Sign Up\n2. Log In\n3. password\n4. Message to a friend\n5. Exit\n")   
        if user_input == '1':
            self.sign_up()
        elif user_input == '2':
            self.sign_in()
        elif user_input == '3':
            self.reset_password()
        elif user_input == '4':
            self.send_message()
        elif user_input == '5':
            print("Thank you for using ChatBook. Goodbye!")
            exit()
        else:
            print("Invalid option. Please try again.")
            self.menu()
    
    def sign_up(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        self.email = self.username + "@chatbook.com"
        print("Sign up successful! You can now log in.")
        print(f"Your email is: {self.email}")
        print(f'your password is: {self.password}')
        self.menu()    
    def sign_in(self):
        if self.username=='' and self.password=='':
                print("Sign in successful!")
                self.loggdin = True             
        else:
            uname = input("Enter your username: ")
            pwd = input("Enter your password: ")
            if uname ==self.username and pwd == self.password:
                print("Sign in successful!")
                self.loggdin = True
            else:
                print("Invalid username or password. Please try again.")
                self.menu()
            
            
            
            
obj = chatbook()
        