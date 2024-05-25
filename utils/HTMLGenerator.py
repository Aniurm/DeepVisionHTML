F = open("devops.html", "a")
F.truncate(0)
Declaration = ["<!DOCTYPE html><html><body>\n"]
Header = ["<h1 style='font-family:Montserrat'>My First Heading</h1>\n"]
Short_Paragraph = ["<p style='font-family:Montserrat'>My first paragraph - This is a really cool way to quickly design and build websites...Don't you think?</p>\n"]
Long_Paragraph = ["<p style='font-family:Montserrat'>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>\n"]
Button = ["<button type='button' style='font-family:Montserrat'>Click Me!</button>\n"]
Banner = ["<img src='download.png' alt='Trulli' width='1200' height='224'>\n"]
Form = ["<h1  style='font-family:Montserrat'>Sign Up</h1><form action='/action_page.php'> <label for='fname' style='font-family:Montserrat'>First name: </label><input type='text' id='fname' name='fname'><br><br> <label for='lname'  style='font-family:Montserrat'>Last name: </label><input type='text' id='lname' name='lname'><br><br> <input type='submit' value='Submit' style='font-family:Montserrat'></form> "]
Logo = ["<img src='Logo.png' alt='Trulli' width='550' height='124'>\n"]

F.writelines(Declaration)
F.writelines(Banner_Image)
F.writelines(Header)
F.writelines(Short_Paragraph)
F.writelines(Button)
F.writelines(Long_Paragraph)
F.writelines(Form)
F.writelines(Logo)
F.close()