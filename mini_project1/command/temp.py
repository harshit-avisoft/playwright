 # tags , parallel execution , allure , pass loops in feature file , run in different browser
 
#  PS C:\Users\pc\Documents\playwright\mini_project1> & C:/Users/pc/Documents/playwright/venv/Scripts/Activate.ps1
# (venv) PS C:\Users\pc\Documents\playwright\mini_project1> behave
# always run in virtual environment (venv)

# (venv) PS C:\Users\pc\Documents\playwright\mini_project1> behavex features --parallel-processes 2

# (venv) PS C:\Users\pc\Documents\playwright\mini_project1> behave -f allure_behave.formatter:AllureFormatter -o allure-results features
# (venv) PS C:\Users\pc\Documents\playwright\mini_project1> allure serve allure-results
# (venv) PS C:\Users\pc\Documents\playwright\mini_project1> allure generate allure-results -o allure-report --clean

# using allure with behavex 
# behavex features --parallel-processes 2 -o allure-results
# allure serve allure-results

#  Why BehaveX command does NOT need formatter

# BehaveX automatically registers Allure formatter, so you don’t need:

# -f allure_behave.formatter:AllureFormatter